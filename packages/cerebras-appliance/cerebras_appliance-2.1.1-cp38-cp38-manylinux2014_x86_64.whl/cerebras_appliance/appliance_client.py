# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

""" GRPC Client Used by Framework User to connect to Coordinator
"""
import copy
import json
import logging
import os
import queue
import signal
import threading
from dataclasses import dataclass
from typing import Any, Generator, List, Optional, Tuple, Union

import dill
import grpc
import numpy as np
from grpc import ChannelCredentials
from grpc._channel import _InactiveRpcError

from cerebras_appliance import logger
from cerebras_appliance.data.dtypes import bf16, is_bf16
from cerebras_appliance.errors import (
    ApplianceClientException,
    ApplianceRequestCancelled,
    ApplianceResourceExhausted,
    ApplianceRuntimeServerError,
    ApplianceStallError,
    ApplianceTensorDropped,
    ApplianceUnknownError,
)
from cerebras_appliance.pb.framework.appliance_service_pb2 import (
    DataCheckpointRequest,
    DoneRequest,
    FinalizeRequest,
    GetOutputRequest,
    HeartBeatRequest,
    InitRequest,
    LoadRequest,
    MonitorErrorRequest,
    MsgQueueRequest,
    RunRequest,
    SendCheckGroup,
    SendCheckRequest,
    SendInputRequest,
    StartRequest,
    StartStreamingRequest,
    SyncRequest,
)
from cerebras_appliance.pb.framework.appliance_service_pb2_grpc import (
    ApplianceStub,
)
from cerebras_appliance.pb.workflow.appliance.client.client_config_pb2 import (
    ClientCompileInfo,
    ClientExecuteInfo,
    RecvCRD,
    SendCRD,
)
from cerebras_appliance.pb.workflow.appliance.client.shared_cluster_config_pb2 import (
    GenericSendtoRecv,
)
from cerebras_appliance.pb.workflow.appliance.common.common_config_pb2 import (
    ClusterDetails,
)
from cerebras_appliance.pb.workflow.appliance.common.message_queue_pb2 import (
    ValidTopics,
)
from cerebras_appliance.pb.ws.common_pb2 import (
    WS_RT_DROPPED_TENSOR,
    WS_RT_MONITOR_CLEAN,
    WS_RT_REQUEST_CANCELLED,
    WS_RT_STALL_DETECTED,
    WS_RT_SUCCESS,
    ClockSyncRequest,
    PingRequest,
    PingResponse,
    StatusCode,
)
from cerebras_appliance.pb.ws.rtfx_pb2 import RtFxProto
from cerebras_appliance.utils import version_check

MAX_MESSAGE_LENGTH = (1024 * 1024 * 1024 * 2) - 1024  # 2GB - 1 KB
MAX_TRANSFER_BYTES = 256 * 1024 * 1024  # Use 256MiB chunks

RETRY_POLICY = {
    "methodConfig": [
        {
            "name": [{"service": "cerebras.Appliance"}],
            "retryPolicy": {
                "maxAttempts": 5,
                "initialBackoff": "2s",
                "maxBackoff": "10s",
                "backoffMultiplier": 2,
                "retryableStatusCodes": [
                    "UNAVAILABLE",
                    "UNKNOWN",
                    "RESOURCE_EXHAUSTED",
                ],
            },
        }
    ]
}


@dataclass
class HeartBeatOptions:
    """Options to control appliance heartbeat signals"""

    cycle_seconds: int = 30
    cycle_threshold: int = 10

    def __post_init__(self) -> None:
        if self.cycle_seconds <= 0:
            raise ValueError(
                f"`cycle_seconds` must be greater than 0. "
                f"Got {self.cycle_seconds}."
            )
        if self.cycle_threshold <= 0:
            raise ValueError(
                f"`cycle_threshold` must be greater than 0. "
                f"Got {self.cycle_threshold}."
            )


class ApplianceClient:
    """Manages connections to Coordinator GRPC Server"""

    def __init__(
        self,
        crd_address: str,
        credentials: Optional[ChannelCredentials] = None,
        default_authority: Optional[str] = None,
        disable_stall_detection: bool = False,
        heartbeat_options: Optional[HeartBeatOptions] = None,
        execution_strategy: Optional[int] = None,
        disable_version_check: bool = False,
        retry_small_payload: bool = False,
        max_transfer_bytes: Optional[int] = None,
    ) -> None:
        """Creates initial connection and configures client.
        Args:
            crd_address: Address of grpc server to conect to.
            credentials: GRPC Channel Credentials to establish secure channel.
            dafault_authority: Authority to authorize communication.
            disable_stall_detection: Flag to disable stall detection.
            heartbeat_options: Options to control appliance heartbeat signals.
                If None, heartbeat is disabled.
            execution_strategy (ExecutionStrategy): The execution strategy to
                initialize the server for. This is either pipeline or weight
                streaming. If None, it assumes the server has already been
                initialized with the appropriate execution strategy. Defaults to
                None.
        """
        self.grpc_fork_support_value = os.environ.get(
            'GRPC_ENABLE_FORK_SUPPORT', None
        )
        # SW-89390: To suppress the spam messages from gRPC library
        os.environ.update({'GRPC_ENABLE_FORK_SUPPORT': '0'})
        self.retry_small_payload = retry_small_payload
        self.max_transfer_bytes = max_transfer_bytes
        if not max_transfer_bytes:
            self.max_transfer_bytes = MAX_TRANSFER_BYTES
        self.stall_detection_enabled = not disable_stall_detection
        channel_options = [
            ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
            ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
            ('grpc.max_metadata_size', MAX_MESSAGE_LENGTH),
            ("grpc.per_rpc_retry_buffer_size", MAX_MESSAGE_LENGTH),
            ("grpc.enable_retries", 1),  # Only required until grpc > 1.39
            ('grpc.service_config', json.dumps(RETRY_POLICY)),
        ]
        if default_authority is not None:
            channel_options.append(
                ('grpc.default_authority', default_authority)
            )
        if credentials:
            self._channel = grpc.secure_channel(
                crd_address, credentials, options=channel_options,
            )
        else:
            self._channel = grpc.insecure_channel(
                crd_address, options=channel_options,
            )
        self.stub = ApplianceStub(self._channel)
        logger.debug(f"ApplianceStub started at address: {crd_address}")

        # Clock Sync on connection to verify server in READY state
        self.clock_sync()

        # Initialize service for given execution strategy
        if execution_strategy is not None:
            logger.debug("Sending start request")
            start_response = self.stub.UnaryStart(
                StartRequest(
                    execution_strategy=execution_strategy,
                    client_version_enforce=True,
                )
            )
            _check_rpc_status(start_response)
            if not disable_version_check:
                crd_version = start_response.version_info.version
                crd_hash = start_response.version_info.githash
                version_check("CBCORE", crd_version, crd_hash)

        self._heartbeat_stop = threading.Event()
        if heartbeat_options is not None:
            if not isinstance(heartbeat_options, HeartBeatOptions):
                raise ValueError(
                    f"`heartbeat_options` must either be `None` (to disable "
                    f"hearbeats or an object of type `HeartBeatOptions`, "
                    f"but got `{type(heartbeat_options)}`."
                )

            logger.debug(
                f"Starting heartbeat thread. Heartbeat requests will be sent "
                f"every {heartbeat_options.cycle_seconds} seconds."
            )
            threading.Thread(
                target=_heartbeat_thread,
                args=(
                    self.stub,
                    copy.deepcopy(heartbeat_options),
                    self._heartbeat_stop,
                ),
                name="heartbeat_thread",
                daemon=True,
            ).start()

        # Monitor Coordinator for potential Runtime server error
        self.monitor_result = None
        # Register SIGURG handler for alarm sent from monitor callback
        self.pid = os.getpid()
        if threading.current_thread() is threading.main_thread():
            # Can only use signal handler in main thread
            signal.signal(signal.SIGURG, self._alarm_handler)
        # Track activities occuring during shutdown
        self._shut_down = threading.Event()

    def __del__(self):
        self.stop_heartbeat()

        if self.grpc_fork_support_value is not None:
            os.environ.update(
                {'GRPC_ENABLE_FORK_SUPPORT': self.grpc_fork_support_value}
            )
        else:
            os.environ.unsetenv('GRPC_ENABLE_FORK_SUPPORT')

    def clock_sync(self) -> bool:
        """Command to do a clock sync with Coordinator Server"""
        response = self.stub.UnaryClockSync(
            ClockSyncRequest(), wait_for_ready=True
        )
        return response.code == WS_RT_SUCCESS

    def stop_heartbeat(self) -> None:
        """Command to stop heart beat with Coordinator Server"""
        if not self._heartbeat_stop.is_set():
            logger.debug("Signalling heartbeat thread to stop")
            self._heartbeat_stop.set()

    def stop_monitor_error(self) -> None:
        """Command to stop async thread monitoring Coordinator Errors"""
        logger.debug("Stop monitor error")
        self._shut_down.set()

    def ping(self, timeout=None) -> bool:
        """Command to ping Coordinator Server"""
        logger.debug("Pinging coordinator")
        request = PingRequest(message="Hello, Coordinator!")
        response = self.stub.UnaryPing(request, timeout=timeout)
        logger.debug("Pinged coordinator")
        return response.code == WS_RT_SUCCESS

    def ping_async(self) -> bool:
        """Command to ping Coordinator Server asynchronously"""
        response = PingResponse()
        ping_event = threading.Event()

        def process_response(future):
            response = future.result()
            logger.debug(f"Ping response code: {response.code}")
            logger.debug(f"Ping response message: {response.message}")
            ping_event.set()

        logger.debug("Pinging coordinator")
        request = PingRequest(message="Hello, Coordinator!")
        call_future = self.stub.UnaryPing.future(request, wait_for_ready=True)
        call_future.add_done_callback(process_response)
        ping_event.wait()
        logger.debug("Pinged coordinator")
        return response.code == WS_RT_SUCCESS  # pylint: disable=no-member

    @property
    def shutdown(self):
        """Shutdown event to avoid access to server after termination"""
        return self._shut_down

    def done(self, timeout=300) -> bool:
        """Command to shutdown Coordinator Server"""
        success = False
        logger.debug("Sending done request")
        self._shut_down.set()
        try:
            response = self.stub.UnaryDone(DoneRequest(), timeout=timeout)
        except grpc.RpcError as rpc_error:
            rpc_error_code = rpc_error.code()  # pylint: disable=no-member
            if rpc_error_code == grpc.StatusCode.DEADLINE_EXCEEDED:
                logger.debug(
                    f"{timeout}-sec deadline exceeded,"
                    "Check whether the server stub is live and able to receive"
                    "requests from the client."
                )
            elif rpc_error_code == grpc.StatusCode.UNAVAILABLE:
                logger.debug(
                    "Coordinator is unavailable,"
                    "Check whether the server stub is live and"
                    "able to receive requests from the client."
                )
                success = True
            else:
                logger.debug(
                    f"RPC error code was: {rpc_error_code},"
                    "Check whether the server stub is live"
                    "and able to receive requests from the client."
                )
        else:
            logger.debug(f"Response code: {response.code}")
            logger.debug(f"Response message: {response.message}")
            success = response.code == WS_RT_SUCCESS
        self.stop_heartbeat()
        return success

    def send_artifacts(self, request: SendCRD) -> RecvCRD:
        """Command to send artifacts to Coordinator"""
        logger.debug("Sending init request")
        response = self.stub.RecvArtifacts(request)
        logger.debug(f"Compile dir: {response.cache_compile_dir}")
        return response

    def finalize(self, request: FinalizeRequest) -> None:
        """Finalize the run and allow server to run any cleanup actions."""
        logger.debug("Sending finalize request")
        response = self.stub.UnaryFinalize(request)
        _check_rpc_status(response)

    def init_servers(self, request: InitRequest) -> None:
        """Command to initialize Runtime Command and Weight servers"""
        logger.debug("Sending init request")
        response = self.stub.UnaryInit(request)
        _check_rpc_status(response)

    def load_rtir(self, request: LoadRequest) -> None:
        """Command to load RT IR to Runtime Command and Weight servers"""
        logger.debug("Sending load request")
        response = self.stub.UnaryLoad(request)
        _check_rpc_status(response)

    def sync(self) -> None:
        """Command to synchronize Runtime Command and Weight servers"""
        logger.debug("Sending sync request")
        try:
            response = self.stub.UnarySync(SyncRequest(), wait_for_ready=True)
        except grpc.RpcError as rpc_error:
            # pylint: disable=no-member
            rpc_error_code = rpc_error.code()
            # pylint: disable=no-member
            rpc_error_details = rpc_error.details()
            error_msg = (
                f"Received gRPC error ({rpc_error_code}) : "
                f"'{rpc_error_details}' while sending sync request"
            )
            if rpc_error_code == grpc.StatusCode.RESOURCE_EXHAUSTED:
                raise ApplianceResourceExhausted(error_msg) from rpc_error
            else:
                raise ApplianceUnknownError(error_msg) from rpc_error
        _check_rpc_status(response)

    def run_deferred(
        self, num_iterations, checkpoint_freq, activation_freq
    ) -> None:
        """
        Command to run Runtime Command and Weight servers for a given iteration
        """
        logger.debug("Sending run request")
        request = RunRequest(
            num_iterations=num_iterations,
            checkpoint_freq=checkpoint_freq,
            activation_freq=activation_freq,
        )
        response = self.stub.UnaryRun(request, wait_for_ready=True)
        _check_rpc_status(response)

    def start_streaming(self) -> None:
        """Command to put Runtime in streaming mode"""
        logger.debug("Sending start_streaming request")
        response = self.stub.UnaryStartStreaming(
            StartStreamingRequest(), wait_for_ready=True
        )
        _check_rpc_status(response)

    def send_check(
        self, iteration, info_type=SendCheckRequest.InfoType.ID
    ) -> Union[List[int], List[str], List[SendCheckGroup]]:
        """
        Command to check which tensors are expected by Runtime Weight servers
        """
        logger.debug("Sending send_check request")
        request = SendCheckRequest(iteration=iteration, info_type=info_type)
        response = self.stub.UnarySendCheck(request, wait_for_ready=True)
        _check_rpc_status(response)
        if info_type == SendCheckRequest.InfoType.ID:
            return response.tensor_ids
        elif info_type == SendCheckRequest.InfoType.NAME:
            return response.tensor_names
        elif info_type == SendCheckRequest.InfoType.GROUP:
            return response.tensor_groups
        else:
            raise ValueError(
                f"Invalid info type: {SendCheckRequest.InfoType.Name(info_type)}"
            )

    def send_weight(
        self,
        iteration: int,
        tensor_info: Union[int, str],
        tensor_value: np.ndarray,
        scalar_broadcast: bool = False,
    ) -> None:
        """Command to send weight tensors to Runtime Weight servers.

        Args:
            iteration: Iteration number that this weight is targeted for.
            tensor_info: Name or ID of the tensor.
            tensor_value: The tensor content.
            scalar_broadcast: If true, the tensor (usually a scalar) will be
                              broadcasted to the larger tensor at server side.
        """
        logger.debug(f"Sending weight tensor `{tensor_info}`")

        # gRPC streaming API logs a generic error message when there's an error.
        # So we cache the exception here and reraise it in the request handler.
        generator_error = None
        flow_control = queue.Queue()

        def request_generator(bytes_per_chunk):
            try:
                yield from _chunked_tensor_stream(
                    flow_control,
                    iteration,
                    tensor_info,
                    tensor_value,
                    bytes_per_chunk,
                    scalar_broadcast,
                )
            except Exception as e:
                nonlocal generator_error
                generator_error = e
                raise

        transfer_bytes = self.max_transfer_bytes
        transfer_retries = 0

        retries = 0
        while True:
            try:
                response = None
                for response in self.stub.SendInputBidirStream(
                    request_generator(transfer_bytes)
                ):
                    # Technically Only the first needs to be put in...
                    flow_control.put(response)
                break
            except grpc.RpcError as rpc_error:
                rpc_error_code = rpc_error.code()  # pylint: disable=no-member
                rpc_error_details = (
                    rpc_error.details()  # pylint: disable=no-member
                )
                logger.warning(
                    f"gRPC error code {rpc_error_code} when "
                    f"sending weight tensor {tensor_info}"
                )
                if (
                    isinstance(rpc_error, _InactiveRpcError)
                    and rpc_error_details == "GOAWAY received"
                    and retries < 1
                ):
                    logger.warning(f"Retrying GOAWAY for tensor: {tensor_info}")
                    retries += 1
                elif rpc_error_code == grpc.StatusCode.RESOURCE_EXHAUSTED:
                    # We will retry with smaller chunks if provided via debug_usr.
                    if self.retry_small_payload and transfer_retries < 10:
                        # Clamp transfer bytes down to tensor size
                        transfer_bytes = min(
                            tensor_value.nbytes, transfer_bytes
                        )
                        # Also, keep decreasing by half with every retry
                        transfer_bytes = max(1, transfer_bytes // 2)
                        transfer_retries += 1
                        logger.warning(
                            f"Retrying RESOURCE_EXHAUSTED for tensor "
                            f"'{tensor_info}' for {transfer_retries} time(s)."
                        )
                    else:
                        raise ApplianceResourceExhausted(
                            f"Failed to send weight tensor '{tensor_info}' with "
                            f"{tensor_value.nbytes} bytes at iteration {iteration} "
                            f"due to exhaustion of resources at Coordinator server. "
                            f"Number of transfer retries = {transfer_retries}. "
                            f"Smallest amount of transfer bytes = {transfer_bytes}. "
                        ) from rpc_error
                elif generator_error is not None:
                    raise ApplianceClientException(
                        f"Failed to send weight tensor {tensor_info} at "
                        f"iteration {iteration} due to error when generating "
                        f"requests."
                    ) from generator_error
                elif not self.retry_small_payload and transfer_bytes > 1:
                    raise ApplianceUnknownError(
                        f"Failed to send weight tensor {tensor_info} at "
                        f"iteration {iteration}."
                    ) from rpc_error

        _check_rpc_status(response)

    def recv_output(
        self, iteration, tensor_info: Union[str, int]
    ) -> np.ndarray:
        """Command to receive output tensors from Runtime Weight servers"""
        logger.debug(f"Receiving output tensor {tensor_info}")
        request = GetOutputRequest(iteration=iteration)
        if isinstance(tensor_info, str):
            request.tensor_name = tensor_info
        else:
            request.tensor_id = tensor_info
        # Receive large tensor in chunks
        try:
            dtype = None
            shape = None
            buffer = bytearray()
            for response in self.stub.GetOutputStream(request):
                # The server responded, but we still need to check if
                # GetOutputResponse has any indication for an error
                _check_rpc_status(response)

                assert response.HasField(
                    "rtfx_proto"
                ), "Expects the type of received tensor chunk to be RtFxProto"
                logger.debug(f"Response code: {response.code}")
                logger.debug(f"Response message: {response.message}")
                if dtype is not None:
                    assert dtype == response.rtfx_proto.dtype
                else:
                    dtype = response.rtfx_proto.dtype
                if shape is not None:
                    assert shape == response.rtfx_proto.tensor.shape
                else:
                    shape = response.rtfx_proto.tensor.shape
                buffer.extend(response.rtfx_proto.tensor.data)
        except grpc.RpcError as rpc_error:
            rpc_error_code = rpc_error.code()  # pylint: disable=no-member
            logger.debug(
                f"gRPC error code {rpc_error_code} when "
                f"receiving output tensor {tensor_info}"
            )
            raise ApplianceUnknownError(
                f"Ran into error while receiving output tensor "
                f"{tensor_info} for runtime iteration {iteration}."
            ) from rpc_error

        # Construct np.ndarray
        return _np_from_rtfx(buffer, dtype, shape)

    def monitor_error_async(self, poll_duration: int = 10) -> None:
        """
        Command to monitor Coordinator Server, which also monitors Runtime
        servers for any crashes, assertions, etc.

        Args:
            poll_duration: Seconds to poll for errors before reconnecting
        """

        def run():
            logger.debug("Monitoring Coordinator for Runtime server errors")
            monitor_error_stop = False
            while not monitor_error_stop and not self.shutdown.is_set():
                monitor_error_stop = True
                try:
                    response = self.stub.UnaryMonitorError(
                        MonitorErrorRequest(
                            message="Appliance Client monitoring Coordinator",
                            poll_seconds=poll_duration,
                        ),
                    )
                except grpc.RpcError as rpc_error:
                    # pylint: disable=no-member
                    rpc_error_code = rpc_error.code()

                    # pylint: disable=no-member
                    rpc_error_details = rpc_error.details()
                    # Skip spurious errors after we've triggered shutdown
                    # Ignore RESOURCE_EXHAUSTED since a memory pool may be
                    # exhausted  while transferring weights...
                    if (
                        not self.shutdown.is_set()
                        and self.monitor_result is None
                        and rpc_error_code != grpc.StatusCode.RESOURCE_EXHAUSTED
                    ):
                        self.monitor_result = ApplianceUnknownError(
                            f"Received unexpected gRPC error ({rpc_error_code}) : "
                            f"'{rpc_error_details}' while monitoring Coordinator "
                            f"for Runtime server errors"
                        )
                else:
                    if response.code == WS_RT_SUCCESS:
                        logger.debug(f"Monitoring returned")
                    elif response.code == WS_RT_MONITOR_CLEAN:
                        monitor_error_stop = False
                    elif self.monitor_result is None:
                        self.monitor_result = ApplianceRuntimeServerError(
                            f"Error detected in "
                            f"{ClusterDetails.TaskInfo.TaskType.Name(response.srv_type)} "
                            f"#{response.host_index}. "
                            f"Status code: {StatusCode.Name(response.code)}. "
                            f"Status message: {response.message}"
                        )
            # Send SIGURG to the process that is running ApplianceClient
            os.kill(self.pid, signal.SIGURG)

        threading.Thread(target=run,).start()
        # Start a secondary thread with a delay but before the first thread receives
        # the response back
        threading.Timer(poll_duration // 2, run).start()

    def close(self) -> None:
        """Close GRPC Channel for client"""
        self.stop_heartbeat()
        self._channel.close()

    def transfer_artifacts(self, request: GenericSendtoRecv) -> None:
        """Command to transfer artifacts between servers"""
        logger.debug("Transferring Artifacts")
        response = self.stub.TransferArtifacts(request)
        _check_rpc_status(response)

    def _alarm_handler(self, signum, frame):
        """Handles alarm sent from monitor callback"""
        logger.debug("Inside alarm handler")
        # If monitor is inflight while shutting down can hit closed server
        if self.monitor_result is not None:
            self.stop_heartbeat()
            logger.warning(
                f"Monitor came back with error: '{self.monitor_result}'"
            )
            raise self.monitor_result

    def fetch_dataloader_state(self, current_step: int) -> List[bytes]:
        """Command to fetch state of WRK(s) feeding the input data pipeline
        at the current appliance step."""
        logger.debug(f"Fetching dataloader state")
        request = DataCheckpointRequest(iteration=current_step)
        response = self.stub.UnaryDataCheckpoint(request)
        _check_rpc_status(response)
        return response.state_dict_serialized

    def get_msg(self, topic: ValidTopics, timeout: int = 10):
        """Retrieve Message from Server Message Queue"""
        request = MsgQueueRequest(topic=topic, timeout_seconds=timeout)
        return self.stub.UnaryMsgQueue(request)


def _check_rpc_status(response, name=None, raise_error=True):
    """Raises an exception if gRPC response code is anything but success.

    Args:
        response: gRPC response from appliance service.
        name: Name of the operation to print in debug message.
        raise_error: Raise error if response code is anything but success.
    Raises:
        ApplianceClientException if response code is an error.
    """
    messages = [f"Response code: {response.code}"]
    if hasattr(response, "message"):
        messages.append(f"Response message: {response.message}")

    for msg in messages:
        if name:
            msg = f"{name} {msg}"

        if response.code == WS_RT_SUCCESS or raise_error:
            logger.debug(msg)
        else:
            logger.error(msg)

    if response.code == WS_RT_SUCCESS:
        return

    error_cls = ApplianceStallError
    if response.code == WS_RT_STALL_DETECTED:
        error_cls = ApplianceStallError
    elif response.code == WS_RT_REQUEST_CANCELLED:
        error_cls = ApplianceRequestCancelled
    elif response.code == WS_RT_DROPPED_TENSOR:
        error_cls = ApplianceTensorDropped
    else:
        error_cls = ApplianceUnknownError

    raise error_cls(
        getattr(
            response,
            "message",
            f"Server call failed with {StatusCode.Name(response.code)}",
        )
    )


def _chunked_tensor_stream(
    flow_control: queue.Queue,
    iteration: int,
    tensor_name: Union[int, str],
    tensor_value: np.ndarray,
    bytes_per_chunk: int,
    scalar_broadcast: bool = False,
) -> Generator[SendInputRequest, None, None]:
    """Chunks a numpy array into a stream of SendInputRequests.

    gRPC has a 2GB transfer size limit. As such, any tensor over this limit is
    chunked into a list of smaller tensors that can be streamed to a gRPC
    endpoint.

    Args:
        iteration: Iteration number that this tensor is targeted for.
        tensor_name: Name or ID of the tensor.
        tensor_value: The tensor content.
        bytes_per_chunk: Number of bytes per chunk of tensor.
        scalar_broadcast: If true, the tensor (usually a scalar) will be
                          broadcasted to the larger tensor at server side.
    """
    rtfx_dtype = _rtfx_dtype_from_np_dtype(tensor_value.dtype)
    if rtfx_dtype == RtFxProto.T_I1:
        # I1 needs to be encoded as int16
        tensor_value = tensor_value.astype(np.int16)

    tensor_size = tensor_value.size
    tensor_shape = tensor_value.shape
    num_dims = tensor_value.ndim
    num_bytes = tensor_value.nbytes
    num_chunks = 1
    if num_bytes > bytes_per_chunk:
        assert num_dims, "Expects an array"
        logging.debug(f"Shape of tensor '{tensor_name}': {tensor_shape}")
        logging.debug(f"Size of tensor '{tensor_name}': {tensor_size}")
        logging.debug(f"Storage size of tensor '{tensor_name}': {num_bytes}")
        # We will use the number of chunks that is power of 2
        num_chunks = num_bytes // bytes_per_chunk
        num_chunks = 1 << num_chunks.bit_length()
        # We are also making sure every chunk is equal in size
        if num_bytes % num_chunks:
            logging.debug(
                f"Tensor '{tensor_name}' with size of {num_bytes} bytes can't "
                "be put into chunks with an equal size. Dropping back to "
                "sending entire tensor in a single chunk."
            )
            num_chunks = 1
    logging.debug(f"Number of chunks to send: {num_chunks}")
    chunk_size = tensor_size // num_chunks
    tensor_nbytes = num_bytes // num_chunks
    logging.debug(f"Number of items in each chunk: {chunk_size}")
    logging.debug(f"Number of bytes in each chunk: {tensor_nbytes}")
    # Here, we will try to avoid using `np.ravel()` as well by working on
    # memory view directly. Iterating over memory view might be tricky.
    # However, most of the large tensors have the similar dimensionality.
    # Therefore, we can start with very simple special case. We will improve
    # the special cases later if needed.
    use_ravel = True
    chunk_offset = chunk_size
    # Special case where we can avoid `np.ravel()`
    if num_dims == 2:
        row_count = tensor_shape[0]
        col_count = tensor_shape[1]
        if row_count >= num_chunks and row_count % num_chunks == 0:
            if col_count < chunk_size and chunk_size % col_count == 0:
                use_ravel = False
                chunk_offset = chunk_size // col_count
    if use_ravel:
        logging.debug(f"Using 'ravel()' for tensor '{tensor_name}'")
        tensor_memory_view = tensor_value.ravel(order='A').data
    else:
        logging.debug(f"Skipping 'ravel()' for tensor '{tensor_name}'")
        tensor_memory_view = tensor_value.data
    # Now, we are putting the weight tensor into chunk(s)
    for k in range(num_chunks):
        start = k * chunk_offset
        end = start + chunk_offset

        request = SendInputRequest(
            iteration=iteration,
            num_bytes=tensor_nbytes,
            has_more=k < num_chunks - 1,
        )

        if isinstance(tensor_name, str):
            request.tensor_name = tensor_name
        elif isinstance(tensor_name, int):
            request.tensor_id = tensor_name
        else:
            raise TypeError(
                f"Expected tensor info to be an integer ID or string name, "
                f"but got {type(tensor_name)}"
            )

        request.rtfx_proto.dtype = rtfx_dtype
        if scalar_broadcast:
            # Send the original tensor name
            request.rtfx_proto.scalar.name = str(tensor_name)
            request.rtfx_proto.scalar.data = tensor_memory_view[
                start:end
            ].tobytes()
        else:
            # Send the original tensor name and shape
            request.rtfx_proto.tensor.name = str(tensor_name)
            request.rtfx_proto.tensor.shape.extend(tensor_shape)

            if k == 0:
                # Send an empty request so coordinator can allocate buffers and
                # backpressure gRPC if needed
                has_more = request.has_more
                request.has_more = True
                logging.debug(f"Sending metadata only chunk for {tensor_name}")
                yield request
                request.has_more = has_more
                # Block until server gives us the first "go ahread" response.
                _ = flow_control.get()
                logging.debug(f"Received go ahead for {tensor_name}")
                # continue!
            request.rtfx_proto.tensor.data = tensor_memory_view[
                start:end
            ].tobytes()

        logging.debug(f"Sending chunk {k} for {tensor_name}")
        yield request


def _rtfx_dtype_from_np_dtype(np_dtype):
    assert isinstance(np_dtype, np.dtype), "Numpy dtype expected"
    if is_bf16(np_dtype):
        return RtFxProto.T_BF16
    elif np_dtype == bool:
        return RtFxProto.T_I1  # BUT NOTE: it needs casting
    elif np_dtype == np.int16:
        return RtFxProto.T_I16
    elif np_dtype == np.int32:
        return RtFxProto.T_I32
    elif np_dtype == np.int64:
        return RtFxProto.T_I64
    elif np_dtype == np.uint8:
        return RtFxProto.T_U8
    elif np_dtype == np.uint16:
        return RtFxProto.T_U16
    elif np_dtype == np.uint32:
        return RtFxProto.T_U32
    elif np_dtype == np.uint64:
        return RtFxProto.T_U64
    elif np_dtype == np.float16:
        return RtFxProto.T_F16
    elif np_dtype == np.float32:
        return RtFxProto.T_F32
    elif np_dtype == np.float64:
        return RtFxProto.T_F64
    else:
        assert False, f"Cannot convert np.dtype '{np_dtype}' to RtFxProto dtype"


# Helper functions and gPRC proto constructions we are using to spoof things
def _np_dtype_from_rtfx_dtype(rtfx_dtype):
    if rtfx_dtype == RtFxProto.T_I1:
        return np.int16  # BUT NOTE: it needs casting
    elif rtfx_dtype == RtFxProto.T_I16:
        return np.int16
    elif rtfx_dtype == RtFxProto.T_I32:
        return np.int32
    elif rtfx_dtype == RtFxProto.T_I64:
        return np.int64
    elif rtfx_dtype == RtFxProto.T_U8:
        return np.uint8
    elif rtfx_dtype == RtFxProto.T_U16:
        return np.uint16
    elif rtfx_dtype == RtFxProto.T_U32:
        return np.uint32
    elif rtfx_dtype == RtFxProto.T_U64:
        return np.uint64
    elif rtfx_dtype == RtFxProto.T_F16:
        return np.float16
    elif rtfx_dtype == RtFxProto.T_BF16:
        return bf16
    elif rtfx_dtype == RtFxProto.T_F32:
        return np.float32
    elif rtfx_dtype == RtFxProto.T_F64:
        return np.float64
    else:
        assert False, f"Cannot convert RtFxProto dtype {rtfx_dtype} to np.dtype"


def _np_from_rtfx(
    buffer: bytearray, rtfx_dtype: int, shape: Tuple[int]
) -> np.ndarray:
    """Returns a numpy array from the given buffer with the given rtfx dtype.

    Args:
        buffer: The buffer containing the data.
        rtfx_dtype: The RtFxProto dtype.
        shape: The shape of the tensor.
    Returns:
        The numpy array matching the given buffer.
    """
    # Construct np.ndarray
    dtype = _np_dtype_from_rtfx_dtype(rtfx_dtype)
    logger.debug(f"Buffer size: {len(buffer)}, {dtype = }, {shape = }")
    if not shape:
        shape = []
    array = np.frombuffer(buffer, dtype=dtype).reshape(shape)

    # I1 comes through as int16, but it _should_ be bool...
    # Might need dtype conversion.
    if rtfx_dtype == RtFxProto.T_I1 and array.dtype != bool:
        array = array.astype(bool)

    return array


def _create_compile_info(
    batch_size,
    num_csx,
    max_wgt_servers,
    num_workers_per_csx,
    cirh_str,
    compile_dir,
    max_act_per_csx=1,
):
    """ Helper function to create the ClientCompileInfo protobuf
    """
    compile_request = ClientCompileInfo(
        cirh_content=cirh_str, compile_dir=compile_dir
    )
    compile_request.client_common_info.batch_size = batch_size
    compile_request.client_common_info.num_csx = num_csx
    compile_request.client_common_info.max_wgt_servers = max_wgt_servers
    compile_request.client_common_info.num_workers_per_csx = num_workers_per_csx
    compile_request.client_common_info.max_act_per_csx = max_act_per_csx
    return compile_request


def _create_execute_info(
    input_fn,
    params,
    train_steps,
    ckpt_steps,
    batch_size,
    num_csx,
    cache_compile_dir,
    framework_type,
    mode_key,
    enable_dataloader_checkpointing=False,
    dataloader_state_dict_serialized=None,
):
    """ Helper function to create the ClientExecuteInfo protobuf
    """
    execute_info = ClientExecuteInfo()
    input_fn_serialized = fw_user_serialize(input_fn, name="input_fn")
    logger.debug(f"Input fn serialized: {input_fn_serialized}")
    execute_info.input_fn_serialized = input_fn_serialized
    execute_info.input_params_serialized = fw_user_serialize(
        params, name="params"
    )
    execute_info.total_steps = train_steps
    execute_info.checkpoint_steps = ckpt_steps
    execute_info.client_common_info.batch_size = batch_size
    execute_info.client_common_info.num_csx = num_csx
    execute_info.cache_compile_dir = cache_compile_dir
    execute_info.framework_type.type = framework_type
    execute_info.mode_key = mode_key
    execute_info.enable_dataloader_checkpointing = (
        enable_dataloader_checkpointing
    )
    if dataloader_state_dict_serialized:
        execute_info.dataloader_state_dict_serialized = fw_user_serialize(
            dataloader_state_dict_serialized
        )
    return execute_info


def construct_compile_request(
    batch_size,
    num_csx,
    max_wgt_servers,
    num_workers_per_csx,
    cirh_str,
    compile_dir,
    max_act_per_csx=1,
):
    """ Create a SendCRD proto object with the compile_info only set
    and send an execution request to Coord.

    Right now, we don't have the gPRC communication between fw client and
    coordinator fully setup. We have the proto definitions, but we don't have
    the actual rpcs. So we will be spoofing by only creating the request and not
    actually making any rpc.

    Eventually, we will be calling the pertinent remote function and return the
    response

    TODO: Make this an actual RPC
    """
    compile_info = _create_compile_info(
        batch_size,
        num_csx,
        max_wgt_servers,
        num_workers_per_csx,
        cirh_str,
        compile_dir,
        max_act_per_csx,
    )
    coord_req = SendCRD(compile_info=compile_info,)
    return coord_req


def construct_run_request(
    cache_compile_dir,
    input_fn,
    params,
    batch_size,
    train_steps,
    ckpt_steps,
    num_csx,
    framework_type,
    mode_key,
    enable_dataloader_checkpointing=False,
    dataloader_state_dict_serialized=None,
):
    """ Create a SendCRD proto object with the cache_compile_dir set and
    send an execution request to Coord.

    Right now, we don't have the gPRC communication between fw client and
    coordinator fully setup. We have the proto definitions, but we don't have
    the actual rpcs. So we will be spoofing by only creating the request and not
    actually making any rpc.

    Eventually, we will be calling the pertinent remote function and return the
    response.

    TODO: Make this an actual RPC
    """
    client_execute_info = _create_execute_info(
        input_fn=input_fn,
        params=params,
        train_steps=train_steps,
        ckpt_steps=ckpt_steps,
        batch_size=batch_size,
        num_csx=num_csx,
        cache_compile_dir=cache_compile_dir,
        framework_type=framework_type,
        mode_key=mode_key,
        enable_dataloader_checkpointing=enable_dataloader_checkpointing,
        dataloader_state_dict_serialized=dataloader_state_dict_serialized,
    )
    coord_req = SendCRD(execute_info=client_execute_info,)
    return coord_req


def fw_user_serialize(worker_data: Any, name: str = "object") -> str:
    """Serialized information that client can send the appliance.

    Currently, this handles the input_fn and params for the input_fn.
    These are separate because python can't serialized generators directly,
    so the worker creates the generator locally.

    Args:
        worker_data: Most likely a Callable or Dict, but anything pickleable works.
        name: A user-friendly name for the object being serialized.

    Returns:
        serialized_data: Assumed will be deserialized by worker_deserialize.
    """
    try:
        return dill.dumps(worker_data).hex()
    except Exception as e:
        raise RuntimeError(
            f"Failed to serialize `{name}` to send from the user node to the "
            f"input workers (running in the Wafer-Scale Cluster) due to the "
            f"following error: {e}.\nPlease make sure `{name}` is picklable "
            f"using the `dill` package."
        ) from e


def _heartbeat_thread(
    stub: ApplianceStub,
    options: HeartBeatOptions,
    stop_event: threading.Event,
    timeout: int = 1,
) -> None:
    """Thread that continuously sends heartbeat signals to the Appliance.

    Args:
        stub: The client to use for sending the heartbeat signals.
        options: HeartBeat configuration options.
        stop_event: Event that will stop the heartbeat thread when set.
        timeout: Timeout for the heartbeat RPC.
    """
    failure_count = 0
    first_request = True
    while (first_request and not stop_event.is_set()) or not stop_event.wait(
        options.cycle_seconds
    ):
        first_request = False

        try:
            stub.UnaryHeartBeat(
                HeartBeatRequest(
                    cycle_seconds=options.cycle_seconds,
                    failure_cycle_threshold=options.cycle_threshold,
                ),
                timeout=timeout,
            )
            if failure_count:
                logger.info(
                    f"Heartbeat to the Appliance succeeded after "
                    f"{failure_count} consecutive failures."
                )
            failure_count = 0
        except grpc.RpcError as rpc_error:
            rpc_error_code = rpc_error.code()  # pylint: disable=no-member
            failure_count += 1
            logger.warning(
                f"Heartbeat to the Appliance failed with error code "
                f"`{rpc_error_code.name}` (consecutive failure count: "
                f"{failure_count}). Retrying in {options.cycle_seconds} "
                f"seconds."
            )
            if failure_count == options.cycle_threshold:
                logger.warning(
                    f"Heartbeat failure count, {failure_count}, has exceeded "
                    f"the threshold. The Appliance will likely begin "
                    f"self-destructing soon as it hasn't heard from the client "
                    f"in a while."
                )

    logger.debug("Heartbeat thread stopped.")
