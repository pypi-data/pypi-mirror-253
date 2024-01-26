# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""
HDF5 based checkpoint saver.
"""

from __future__ import annotations

import enum
import json
import os
from inspect import isclass
from typing import Any, Dict, List, Optional
from urllib.parse import quote, unquote  # to escape `/` in tensor names
from warnings import warn

import dill
import h5py as h5
import hdf5plugin
import numpy as np
from numpy import ndarray as nd

from cerebras_appliance.data.dtypes import bf16, is_bf16
from cerebras_appliance.log import ClassLogger, named_class_logger
from cerebras_appliance.saver.base_saver import BaseSaver
from cerebras_appliance.utils.misc import is_cerebras_available

H5_TYPE_KEY = "__H5_TYPE__"


class Storage(str, enum.Enum):
    """Strategy to store tensors."""

    TENSOR = "COMPACT"  # store tensor along with metadata
    PROTOBUF = "EXTERNAL"  # storage is external file
    SHARDED = "VIRTUAL"  # multiple datasets are used to represent tensors.

    @staticmethod
    def get_storage_type(name: str):
        """Returns the StorageType enum for the given storage string"""
        # TODO this is probably redundant
        return Storage(name.upper())


class Compression(str, enum.Enum):
    """
    Compression to use for storage
    """

    NONE = None
    GZIP = "gzip"
    SZIP = "szip"
    LZF = "lzf"
    LZ4 = "lz4"

    @staticmethod
    def get_compression(name: str):
        """Returns Compression Enum for the given string."""
        return Compression(name.lower())

    @classmethod
    def _missing_(cls, value):
        """Default to no compression."""
        return Compression.NONE

    @staticmethod
    def get_compression_options(compression: Compression):
        """Return compression options for the given compression type."""

        if compression == Compression.GZIP:
            return 0  # TODO make this configurable
        if compression == Compression.SZIP:
            return ''
        if compression == Compression.LZF:
            return None
        else:
            return ''


DEFAULT_NBYTES: int = (1024 * 1024)  # 1 MB
DEFAULT_STORAGE_TYPE: Storage = Storage.TENSOR
DEFAULT_COMPRESSION: Compression = Compression.LZ4


@named_class_logger("H5Saver")
class H5Saver(BaseSaver, ClassLogger):
    """
    HDF5 format backed checkpointing class to save/restore numpy arrays and scalars.
    Checkpoint for each step is saved as a separate H5 file objects with each tensor
    in a separate hdf5 dataset allowing partial access of checkpoint files.
    """

    CKPT_INFO = 'ckpt_info'
    CKPT_PATHS = 'ckpt_paths'

    def __init__(
        self,
        nbytes: int = DEFAULT_NBYTES,
        storage_type: Storage = DEFAULT_STORAGE_TYPE,
        compression: Compression = DEFAULT_COMPRESSION,
        max_store: Optional[int] = None,
    ):
        """
        Constructs a H5 Saver object.

        Args:
            nbytes: number of bytes to load into memory from hdf5 datasets, defaults to 1 MB
            storage_type: tensor storage strategy, defaults to Storage.TENSOR tensor
            compression: Compression strategy, defaults to Compression.GZIP
            max_store: maximum number of checkpoints to store
        """
        super().__init__()
        # these should only be set only when creating
        # except for nbytes, other config parameters cannot change
        self._ckpt_info = {
            'nbytes': nbytes,
            'storage_type': storage_type,
            'compression': compression,
            H5Saver.CKPT_PATHS: [None],
        }
        if max_store is not None:
            if (not isinstance(max_store, int)) or max_store <= 0:
                raise ValueError(
                    f"max_store must be None or int > 0. Got {max_store} instead."
                )
        self.max_store = max_store
        self._ckpt_dir = None

    def _save_ckpt_info(self, ckpt_info_file: str, ckpt_path: str):
        """Save ckpt_info if last checkpoint path changed."""
        # Pull existing meta data
        prev_ckpt_info = self.get_ckpt_info(ckpt_info_file)
        if prev_ckpt_info is not None:
            self._ckpt_info[H5Saver.CKPT_PATHS] = prev_ckpt_info[
                H5Saver.CKPT_PATHS
            ]

        ckpt_paths = self._ckpt_info[H5Saver.CKPT_PATHS]
        self._ckpt_dir = os.path.dirname(ckpt_info_file)
        ckpt_path = os.path.relpath(ckpt_path, self._ckpt_dir)
        if ckpt_paths and ckpt_paths[-1] != ckpt_path:
            self._ckpt_info[H5Saver.CKPT_PATHS].append(ckpt_path)
            while (
                self.max_store
                and len(self._ckpt_info[H5Saver.CKPT_PATHS]) > self.max_store
            ):
                drop_ckpt = self._ckpt_info[H5Saver.CKPT_PATHS].pop(0)
                if drop_ckpt:
                    drop_ckpt = os.path.join(self._ckpt_dir, drop_ckpt)
                    if os.path.exists(drop_ckpt):
                        self.logger.info(
                            f"Erasing {drop_ckpt} to maintain "
                            f"{self.max_store} checkpoints."
                        )
                        try:
                            os.remove(drop_ckpt)
                        except OSError as e:
                            warn(
                                f"Failed to clean up old checkpoint {drop_ckpt} due to error: {e}"
                            )
            with h5.File(ckpt_info_file, "w") as f:
                f.attrs['ckpt_info'] = json.dumps(self._ckpt_info)

    def update_ckpt_info(self, ckpt_path: str):
        """Manual call to _save_ckpt_info. Used after calling save(..., save_metadata=False)."""
        ckpt_info_file = os.path.join(
            os.path.dirname(ckpt_path), H5Saver.CKPT_INFO
        )
        self._save_ckpt_info(ckpt_info_file, ckpt_path)

    # pylint: disable=no-self-use
    def _create_ckpt_dirs(self, ckpt_path: str):
        """Create checkpoint directories if it does not exist."""
        parent_dir = os.path.dirname(ckpt_path)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)

    @staticmethod
    def get_ckpt_info(ckpt_info_file: str) -> Dict:
        """Returns checkpoint info as a dictionary from the info file path

        Args:
            ckpt_info_file: file path of ckpt_info file

        Returns:
            Metadata stored in ckpt_info as a dictionary.
        """
        ckpt_info = None
        if os.path.exists(ckpt_info_file):
            with h5.File(ckpt_info_file, "r") as f:
                assert 'ckpt_info' in f.attrs.keys()

                ckpt_info = f.attrs['ckpt_info']
                if isinstance(ckpt_info, bytes):
                    ckpt_info = ckpt_info.decode('utf-8')

                ckpt_info = json.loads(ckpt_info)
        return ckpt_info

    @staticmethod
    def latest_checkpoint(ckpt_dir: str) -> Optional[str]:
        """Returns the latest checkpoint path from a given directory if it exists else None

        Args:
            ckpt_dir: directory in which to look for checkpoints

        Returns:
            Latest checkpoint path.
        """
        ckpts = H5Saver.all_checkpoints(ckpt_dir)
        if ckpts:
            return ckpts[-1]
        return ckpts

    @staticmethod
    def all_checkpoints(ckpt_dir: str) -> Optional[List[str]]:
        """Returns the checkpoints maintained in a given directory if they exist else None
        Args:
            ckpt_dir: directory in which to look for checkpoints

        Returns:
            Latest checkpoint path.
        """
        if not os.path.exists(ckpt_dir):
            return None

        ckpt_info_file = os.path.join(ckpt_dir, H5Saver.CKPT_INFO)

        ckpt_info = H5Saver.get_ckpt_info(ckpt_info_file)
        if ckpt_info and H5Saver.CKPT_PATHS in ckpt_info:
            ckpts = []
            for a_ckpt in ckpt_info[H5Saver.CKPT_PATHS]:
                if a_ckpt and not os.path.isabs(a_ckpt):
                    a_ckpt = os.path.join(ckpt_dir, a_ckpt)

                if a_ckpt and os.path.exists(a_ckpt):
                    ckpts.append(a_ckpt)

            if ckpts:
                return ckpts
        return None

    def save_tensor(
        self, ckpt_file: str, tensor_name: str, tensor_value: nd,
    ) -> None:
        """Saves a tensor value as a separate h5 dataset for the given file. Does not
        automatically update ckpt_info.

        Args:
            ckpt_file: where to write checkpoint
            tensor_name: name of the tensor, this will be used as the h5 dataset name
            tensor_value: numpy ndarray or numpy scalar
        """
        self.save(
            ckpt_file, {tensor_name: tensor_value}, save_metadata=False,
        )

    def load_tensor(self, ckpt_path: str, tensor_name: str) -> nd:
        """Loads the tensor with given name from the path provided.

        Args:
            ckpt_path: a specific checkpoint
            tensor_name: name of the tensor to get

        Returns:
            Tensor value
        """
        return self.load(ckpt_path, [tensor_name])[tensor_name]

    @staticmethod
    def tensor_names(ckpt_path: str) -> List[str]:
        """ Returns all the tensor names for a given checkpoint.

        Args:
            ckpt_path: a specific checkpoint

        Returns:
            List of tensor names
        """
        tensor_names = []
        ckpt_file = ckpt_path
        if os.path.exists(ckpt_file):
            with h5.File(ckpt_file, 'r') as f:
                tensor_names = [unquote(x) for x in f.keys()]
        return tensor_names

    def save(
        self,
        ckpt_file: str,
        tensor_dict: Dict[str, nd],
        save_metadata: bool = True,
    ) -> str:
        """Save tensor_dict to provided file

        Args:
            ckpt_file: where to write checkpoint
            tensor_dict: tensor_name, numpy ndarray or numpy scalar pairs
            save_metadata: whether or not to save to ckpt_info when saving tensors

        Returns:
            checkpoint file path
        """
        ckpt_info_file = os.path.join(
            os.path.dirname(ckpt_file), H5Saver.CKPT_INFO
        )
        if self._ckpt_info['compression'] == Compression.NONE:
            compress_opts = {}
        elif self._ckpt_info['compression'] == Compression.LZ4:
            compress_opts = hdf5plugin.LZ4()
        else:
            compress_opts = {
                "compression": self._ckpt_info['compression'],
                "compression_opts": Compression.get_compression_options(
                    self._ckpt_info['compression']
                ),
            }
        self._create_ckpt_dirs(ckpt_file)
        with h5.File(ckpt_file, "a") as f:
            for name, val in tensor_dict.items():
                self._save_tensor_to_checkpoint(f, name, val, compress_opts)
            if save_metadata:
                self._save_ckpt_info(ckpt_info_file, ckpt_file)

        return ckpt_file

    def _save_tensor_to_checkpoint(
        self, f: h5.File, tensor_name: str, tensor: nd, compression_opts: Dict
    ):
        self.logger.debug(
            f"Saving tensor `{tensor_name}` with type `{type(tensor)}`"
        )
        h5_type = SUPPORTED_H5_TYPES.get(type(tensor))
        if h5_type is None:
            self.logger.debug(
                f"Unsupported type for {tensor_name}: {type(tensor)}. "
                f"Falling back to generic python object saver"
            )
            h5_type = SUPPORTED_H5_TYPES[type]

        try:
            tensor_name = quote(tensor_name, safe='')
            save_type = h5_type.save(tensor, f, tensor_name, **compression_opts)
            if save_type is None:
                save_type = h5_type
            else:
                assert isinstance(save_type, type)
            # Save class name that was used to save
            # Note: if f[tensor_name] is an external link, setting the attr
            # actually changes the attr on the target file instead of this file.
            f[tensor_name].attrs[H5_TYPE_KEY] = save_type.__name__

            if f[tensor_name].external is not None:
                warning_message = (
                    "Saving tensors using external files may cause undefined "
                    "behavior during loading."
                )
                if is_cerebras_available():
                    warning_message += " Please see SW-98658 for more details."

                warn(warning_message)

                for filepath, _offset, size in f[tensor_name].external:
                    if size > 2 ** 30:
                        raise ValueError(
                            f"External size is too large for file {filepath}. "
                            f"This will cause issues when loading the value from "
                            f"the checkpoint. Please split the external file into "
                            f"smaller chunks."
                        )

        except Exception as e:
            raise RuntimeError(
                f"Failed to save {tensor_name} with type {type(tensor)}."
            ) from e

    def create_links(
        self, file_name: str, original_index: str, aliases: List[str]
    ):
        """Create soft link for duplicate entries with different names"""
        if aliases:
            with h5.File(file_name, "a") as f:
                for index in aliases:
                    f[index] = f[original_index]

    def load(
        self,
        ckpt_file: Optional[str] = None,
        tensor_names: Optional[List[str]] = None,
    ) -> Dict[str, nd]:
        """Load all tensors for the given checkpoint or from the last_ckpt step.

        Args:
            ckpt_file: checkpoint to load
            tensor_names: which tensors to load (Defaults to all)

        Returns:
            Mapping from tensor_name to tensor values
        """
        if not ckpt_file:
            ckpt_file = self._ckpt_info[H5Saver.CKPT_PATHS][-1]
            if not os.path.isabs(ckpt_file):
                ckpt_file = os.path.join(self._ckpt_dir, ckpt_file)
        assert os.path.exists(
            ckpt_file
        ), f"Could not find checkpoint: {ckpt_file}"
        tensor_dict = {}
        with h5.File(ckpt_file, "r") as f:
            # Provided names are unquoted so unquote for consistency
            keys = [unquote(name) for name in f.keys()]
            if tensor_names is None:
                tensor_names = keys

            keys = set(keys)

            for name in tensor_names:
                if name not in keys:
                    raise KeyError(
                        f"Could not find key `{name}` in checkpoint {ckpt_file}"
                    )

                dset = f[quote(name, safe='')]

                if dset.external is not None:
                    for filepath, _offset, size in dset.external:
                        if size > 2 ** 30:
                            error_message = (
                                f"External size is too large for file {filepath}. "
                                f"This will cause issues when loading the value from "
                                f"the checkpoint."
                            )
                            if is_cerebras_available():
                                error_message += (
                                    " Please see SW-98658 for more details."
                                )

                            raise ValueError(error_message)

                try:
                    tensor_dict[name] = self._load_tensor_from_checkpoint(
                        f, quote(name, safe='')
                    )
                except OSError as e:
                    if not dset.external:
                        raise
                    # If the dataset is external, raise a more helpful
                    # message by adding the external filepaths.
                    files = ", ".join([e[0] for e in dset.external])
                    raise OSError(
                        f"Failed to load tensor `{name}` from "
                        f"HDF5 file `{ckpt_file}`. This tensor's "
                        f"content is expected to be stored in the "
                        f"following external file(s): {files}. Please "
                        f"ensure that the external files are "
                        f"accessible and valid."
                    ) from e

        return tensor_dict

    def _load_tensor_from_checkpoint(self, f: h5.File, key: str) -> Any:
        dset = f[key]

        # Load the value using the saved H5Type class
        h5_type_name = dset.attrs.get(H5_TYPE_KEY, None)
        if h5_type_name is None:
            raise UnknownH5TypeError(f"Could not find H5Type for {key}")

        return self._load_by_typename(h5_type_name, f, key)

    def _load_by_typename(self, h5_type_name: str, f: h5.File, key: str) -> Any:
        """Load the value using the given H5Type class"""
        if h5_type_name not in H5_TYPES_MAP:
            raise KeyError(
                f"Found unsupported H5Type in checkpoint. "
                f"Expected one of {sorted(H5_TYPES_MAP)}. "
                f"Got {h5_type_name}."
            )

        return H5_TYPES_MAP[h5_type_name].load(f, key)

    @staticmethod
    def is_valid_checkpoint(file_path: Optional[str]) -> bool:
        """Check if file is correct format to be a checkpoint"""
        if file_path is None:
            return False
        return h5.is_hdf5(file_path)


SUPPORTED_H5_TYPES = {}
H5_TYPES_MAP = {}


def register_h5_type(*types):
    """Decorator to register H5Type classes to a list of python types"""

    def cls_wrapper(cls):
        if cls.__name__ not in H5_TYPES_MAP:
            H5_TYPES_MAP[cls.__name__] = cls
        elif H5_TYPES_MAP[cls.__name__] is not cls:
            raise RuntimeError(
                f"Cannot register H5Type {cls} as there already exists "
                f"an H5Type named {cls.__name__} registered to "
                f"{H5_TYPES_MAP[cls.__name__]}"
            )
        if not (hasattr(cls, "save") and hasattr(cls, "load")):
            raise TypeError(
                f"Expected H5Type to have static `save` and `load` methods. "
                f"Please implement them"
            )

        for t in types or [cls]:
            assert isclass(t), f"Failed to register H5Type for non-type: {t}"
            SUPPORTED_H5_TYPES[t] = cls
        return cls

    return cls_wrapper


def _get_all_numpy_dtypes():
    def recurse(cls):
        subclasses = cls.__subclasses__()
        if not subclasses:
            yield cls
        for subcls in subclasses:
            yield from recurse(subcls)

    yield from recurse(np.number)


@register_h5_type(np.ndarray, *_get_all_numpy_dtypes())
class NumpyArrayH5Type:
    """Class for saving and loading numpy arrays to and from the H5 checkpoint"""

    @staticmethod
    def save(ndarray, f: h5.File, key: str, **kwargs):
        """Saves a numpy array to the provided H5 file"""
        shape = tuple(ndarray.shape)
        compress_opts = kwargs if shape else {}
        dset = f.require_dataset(
            key, shape, ndarray.dtype, exact=True, **compress_opts
        )
        dset[...] = ndarray
        dset.attrs["is_bfloat16"] = is_bf16(ndarray)

    @staticmethod
    def load(f: h5.File, key: str):
        """Loads the numpy array from the provided H5 file"""
        dset = f[key]
        array = dset[...]
        if dset.attrs.get("is_bfloat16", False):
            if array.dtype != np.uint16 and array.dtype != np.int16:
                raise ValueError(
                    f"Key `{key}` has `is_bfloat16=True` in its spec, but its "
                    f"dtype is {array.dtype} whereas one of `np.uint16` or "
                    f"`np.int16` was expected."
                )
            array = array.view(bf16)
        return array


@register_h5_type(bool, int, float)
class ScalarH5Type:
    """
    Class for saving and loading python numeric scalars to and from the H5
    checkpoint
    """

    @staticmethod
    def save(obj, f: h5.File, key: str, **kwargs):
        """Saves a python scalar to the provided H5 file"""
        val = np.array(obj)
        dset = f.require_dataset(key, (), val.dtype, exact=True)
        dset[...] = val

    @staticmethod
    def load(f: h5.File, key: str):
        """Loads the python scalar from the provided H5 file"""
        return f[key][...].item()


@register_h5_type(str)
class StringH5Type:
    """
    Class for saving and loading python strings to and from the H5 checkpoint
    """

    __key__ = "string_value"

    @staticmethod
    def save(obj, f: h5.File, key: str, **kwargs):
        """Saves a python string to the provided H5 file"""
        dset = f.create_dataset(key, data=h5.Empty("f"))
        dset.attrs[StringH5Type.__key__] = obj

    @staticmethod
    def load(f: h5.File, key: str):
        """Loads the python string from the provided H5 file"""
        return f[key].attrs[StringH5Type.__key__]


@register_h5_type(type(None))
class NoneH5Type:
    """
    Class for saving and loading python Nones to and from the H5 checkpoint
    """

    @staticmethod
    def save(obj, f: h5.File, key: str, **kwargs):
        """Saves a None placeholder to the provided H5 file"""
        f.create_dataset(key, data=h5.Empty("f"))

    @staticmethod
    def load(f: h5.File, key: str):
        """Returns a NoneType object"""
        return None


@register_h5_type(type)
class ObjectH5Type:
    """
    Fallback class for saving and loading arbitrary python objects to and from
    the H5 checkpoint
    """

    __key__ = "object_value"

    @staticmethod
    def save(obj, f: h5.File, key: str, **kwargs):
        """Saves an arbitrary python object to the provided H5 file"""
        dset = f.create_dataset(key, data=h5.Empty("f"))
        dset.attrs[ObjectH5Type.__key__] = dill.dumps(obj).hex()

    @staticmethod
    def load(f: h5.File, key: str):
        """Loads the arbitrary python object from the provided H5 file"""
        return dill.loads(bytes.fromhex(f[key].attrs[ObjectH5Type.__key__]))


class UnknownH5TypeError(Exception):
    """Raised when an unknown H5 type is encountered."""
