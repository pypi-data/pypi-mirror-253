# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""Utilities to simplify run.py usage"""
from typing import List, Optional

import yaml
from google.protobuf import text_format

from cerebras_appliance.pb.workflow.appliance.common.common_config_pb2 import (
    DebugArgs,
)


def get_supported_type_maps(debug_args):
    """Get the ini maps in the DebugArgs for supported types
    """
    ini_maps = {
        bool: debug_args.ini.bools,
        int: debug_args.ini.ints,
        float: debug_args.ini.floats,
        str: debug_args.ini.strings,
    }
    return ini_maps


def write_debug_args(debug_args: DebugArgs, path: str):
    """Appliance mode write debug args file"""
    with open(path, 'w') as f:
        text_format.PrintMessage(debug_args, f)


def get_debug_args(path: Optional[str]) -> DebugArgs:
    """Appliance mode load debug args and apply defaults"""
    debug_args = DebugArgs()
    if path:
        with open(path, 'r') as f:
            text_format.Parse(f.read(), debug_args)
    return debug_args


def set_ini(debug_args: DebugArgs, **kwargs):
    """Set an Debug INI in the DebugArgs"""
    ini_maps = get_supported_type_maps(debug_args)
    for k, v in kwargs.items():
        maps = ini_maps.get(type(v))
        if maps is None:
            raise TypeError(
                f"\"{k}\"={v} is of unsupported type {type(v)}. Only "
                f"{list(ini_maps.keys())} types are supported INI values."
            )
        maps[k] = v


def set_default_ini(debug_args: DebugArgs, **kwargs):
    """Set default INI in the DebugArgs, if INI is not set"""
    ini_maps = get_supported_type_maps(debug_args)

    for k, v in kwargs.items():
        maps = ini_maps.get(type(v))
        if maps is None:
            raise TypeError(
                f"\"{k}\"={v} is of unsupported type {type(v)}. Only "
                f"{list(ini_maps.keys())} types are supported INI values."
            )
        if k not in maps:
            maps[k] = v


def set_ini_from_file(debug_args: DebugArgs, ini_path: str):
    """Read a yaml file containing debug ini and update the given DebugArgs"""
    with open(ini_path, 'r') as f:
        ini = yaml.safe_load(f)
        if ini:
            set_ini(debug_args, **ini)


def update_debug_args_with_job_labels(
    debug_args: DebugArgs, job_labels: Optional[List[str]] = None
):
    """Update debug args with job labels"""
    if not job_labels:
        return

    for label in job_labels:
        tokens = label.split("=")
        label_key = tokens[0]
        label_val = tokens[1]
        debug_args.debug_mgr.labels[label_key] = label_val


def update_debug_args_with_autogen_policy(
    debug_args: DebugArgs, autogen_policy: Optional[str] = None
):
    """Update debug args with autogen policy"""
    if not autogen_policy:
        return

    policy_map = {
        "default": DebugArgs.DebugCRD.AutogenPolicy.DEFAULT,
        "disabled": DebugArgs.DebugCRD.AutogenPolicy.DISABLED,
        "medium": DebugArgs.DebugCRD.AutogenPolicy.MEDIUM,
        "aggressive": DebugArgs.DebugCRD.AutogenPolicy.AGGRESSIVE,
    }

    if autogen_policy in policy_map:
        debug_args.debug_crd.autogen_policy = policy_map[autogen_policy]
    else:
        raise ValueError(
            f"'{autogen_policy}' is an invalid autogen policy. Valid values "
            f"are {policy_map.keys()}."
        )
