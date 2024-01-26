# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""Cerebras Appliance Mode Client"""
from typing import Dict, List, Union

from cerebras_appliance._version import __version__
from cerebras_appliance.log import logger

DEFAULT_COMPILE_DIR = "cached_compile"

# There are three ways appliance dependencies are represented.
#
# dep names: How the dependencies are represented in pip.
#     Uses a dash to separate (ex: cerebras-pytorch).
# pkg names: The python import name. Uses an underscore to
#     separate (ex: cerebras_pytorch).
# whl names: The name of the .whl file. Uses an underscore to
#     separate but may mismatch pkg name
#     (ex: cerebras_pytorch_xla).
#
# _APPLIANCE_DEPS is a mapping from dep name to whl name.
# To get the pkg name: pkg_name = dep_name.replace("-", "_")
_APPLIANCE_DEPS = {
    "cerebras-appliance": "cerebras_appliance",
}


def register_deps(dep_names: Dict[str, str]):
    """Adds to the list of appliance dependencies.

    Args:
        dep_names: a mapping of dependency name to wheel name
    """
    if not isinstance(dep_names, dict):
        raise ValueError("dep_names must be a dict")

    _APPLIANCE_DEPS.update(dep_names)


def get_deps() -> Dict[str, str]:
    """Returns the mapping of appliance dependencies to wheels."""
    return _APPLIANCE_DEPS
