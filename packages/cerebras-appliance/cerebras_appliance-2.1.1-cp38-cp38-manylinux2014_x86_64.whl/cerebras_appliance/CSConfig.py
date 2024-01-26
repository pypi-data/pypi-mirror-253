# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""Cerebras Configuration Class"""
import os
import re
from dataclasses import dataclass
from typing import List, Optional

from cerebras_appliance.cluster.client import MountDir
from cerebras_appliance.cluster.job_timer import JobTimer
from cerebras_appliance.pb.workflow.appliance.common.common_config_pb2 import (
    CSConfigProto,
    DebugArgs,
)


@dataclass
class CSConfig:
    """Hold config details for WS Appliance Mode.

    Args:
            mgmt_address: Address to connect to appliance.
            mgmt_namespace: Namespace of cluster-mgmt software
                for internal multi-version support only.
            credentials_path: Credentials for connecting to appliance.
            num_csx: Number of Cerebras Systems to run on.
            max_wgt_servers: Number of weight servers to support run.
            max_act_per_csx: Number of activation servers per systemA.
            num_workers_per_csx: Number of streaming workers per system.
            transfer_processes: Number of processes to transfer data to/from
                appliance.
            job_time_sec: Time limit for the appliance jobs, not including the queue time.
            mount_dirs: Local storage to mount to appliance (ex. training data).
            python_paths: A list of path that worker pods respect as PYTHONPATH
                in addition to the PYTHONPATH set in the container image.
            job_labels: A list of equal-sign-separated key-value pairs that
                get applied as part of job metadata.
            debug_args: Optional debugging arguments object.
            precision_opt_level: The precision optimization level.
    """

    mgmt_address: Optional[str] = None
    mgmt_namespace: Optional[str] = None
    credentials_path: Optional[str] = None

    num_csx: Optional[int] = None
    max_wgt_servers: Optional[int] = None
    max_act_per_csx: Optional[int] = None
    transfer_processes: Optional[int] = None
    num_workers_per_csx: Optional[int] = None

    job_time_sec: Optional[int] = None
    job_timer: Optional[JobTimer] = None

    mount_dirs: Optional[List[str]] = None
    python_paths: Optional[List[str]] = None
    job_labels: Optional[List[str]] = None

    debug_args: Optional[DebugArgs] = None
    precision_opt_level: Optional[int] = None

    disable_version_check: bool = False

    def __post_init__(self) -> None:
        if self.num_csx is None:
            self.num_csx = 1
        self.invalidate_unsupported_csx(self.num_csx)

        if self.max_act_per_csx is None:
            self.max_act_per_csx = 60

        if self.transfer_processes is None:
            self.transfer_processes = 5

        if self.num_workers_per_csx is None:
            self.num_workers_per_csx = 0

        if self.job_labels is None:
            self.job_labels = []
        else:
            self.job_labels = self.resolve_job_labels(self.job_labels)

        if self.debug_args is None:
            self.debug_args = DebugArgs()

        if self.mount_dirs is not None:
            self.mount_dirs = self.resolve_mount_dirs(self.mount_dirs)
        else:
            self.mount_dirs = []

        if self.python_paths is not None:
            self.python_paths = self.resolve_real_paths(self.python_paths)
        else:
            self.python_paths = []

        if self.max_wgt_servers is None:
            self.max_wgt_servers = 24

        if self.job_time_sec is not None and self.job_time_sec > 0:
            self.job_timer = JobTimer(self.job_time_sec)

    def get_proto(self) -> CSConfigProto:
        """Create CsConfig proto."""
        cs_config = CSConfigProto()

        cs_config.mgmt_address = self.mgmt_address or ""
        cs_config.mgmt_namespace = self.mgmt_namespace or ""
        cs_config.credentials_path = self.credentials_path or ""

        cs_config.num_csx = self.num_csx
        cs_config.max_wgt_servers = self.max_wgt_servers
        cs_config.max_act_per_csx = self.max_act_per_csx
        cs_config.transfer_processes = self.transfer_processes
        cs_config.num_workers_per_csx = self.num_workers_per_csx

        if self.mount_dirs:
            cs_config.mount_dirs.extend([x.path for x in self.mount_dirs])
        if self.python_paths:
            cs_config.python_paths.extend(self.python_paths)
        if self.job_labels:
            cs_config.job_labels.extend(self.job_labels)

        cs_config.debug_args.CopyFrom(self.debug_args)

        cs_config.disable_version_check = self.disable_version_check

        return cs_config

    @staticmethod
    def resolve_mount_dirs(mount_dirs):
        """Convert a list of mount dirs into a list of MountDir instances"""
        s = set()
        for md in mount_dirs:
            real_path = os.path.realpath(md)
            if not os.path.exists(real_path):
                raise ValueError(f"Mount dir {real_path} does not exist")
            s.add(MountDir(path=md, container_path=md))
        return list(s)

    @staticmethod
    def resolve_real_paths(paths):
        """Convert a list of paths into a list of deduped real paths"""
        s = set()
        for x in paths:
            real_path = os.path.realpath(x)
            if not os.path.exists(real_path):
                raise ValueError(f"{real_path} does not exist")
            s.add(real_path)
        return list(s)

    @staticmethod
    def resolve_job_labels(labels):
        """Assert the list of job labels is valid"""
        pattern = r'^([A-Za-z0-9][-A-Za-z0-9_.]{0,61})?[A-Za-z0-9]$'

        def _is_valid(val):
            return re.match(pattern, val) is not None

        resolved_labels = []
        for kv_pair in labels:
            tokens = kv_pair.split("=")
            if len(tokens) != 2:
                raise ValueError(
                    f"'{kv_pair}' is an invalid label. Expecting the label key and "
                    f"the label value to be separated by a single equal sign(=) character."
                )
            label_key = tokens[0]
            label_val = tokens[1]
            if not _is_valid(label_key) or not _is_valid(label_val):
                raise ValueError(
                    f"'{kv_pair}' is an invalid label. Expecting the label key and the label "
                    f"value to match regex '{pattern}'."
                )
            resolved_labels.append(kv_pair)
        return resolved_labels

    @staticmethod
    def invalidate_unsupported_csx(num_csx):
        """
        As of release 1.9, the following set of num_csxs would yield imbalanced
        BR tree and are currently not supported.
        https://cerebras.atlassian.net/browse/SW-96216
        """

        # This is a list of unsupported csxs for up to 16-CS.
        unsupported_csxs = set([5, 6, 7, 9, 10, 13])
        if num_csx in unsupported_csxs:
            raise ValueError(
                f"{num_csx} would yield imbalanced BR trees and "
                "is currently not supported"
            )
