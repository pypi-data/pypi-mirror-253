# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""
utils file for miscellaneous functions and classes needed
"""
import json
import logging
import os
import subprocess
import sys
import time
from contextlib import contextmanager
from functools import lru_cache
from importlib.util import find_spec
from typing import Dict

from cerebras_appliance import get_deps
from cerebras_appliance._version import __githash__, __version__
from cerebras_appliance.errors import ApplianceVersionError


class ProfileStats(object):
    """Class for profiling one metric and providing aggregate stats."""

    def __init__(self, name):
        """
        Construct a `ProfileStats` instance.
        """
        self.name = name
        self._count = 0
        self._min = float("inf")
        self._max = 0.0
        self._total = 0.0

        self.is_running = False
        self._start_time = 0.0
        self._round_precision = 7

    @property
    def count(self):
        """
        Returns total number of times `start()` was called.
        """
        return self._count

    @property
    def min(self):
        """
        Returns minimum duration in seconds.
        """
        if self._min != float("inf"):
            return self._to_seconds(self._min)
        else:
            return 0.0

    @property
    def max(self):
        """
        Returns maximum duration in seconds.
        """
        return self._to_seconds(self._max)

    @property
    def total(self):
        """
        Returns aggregate duration in seconds.
        """
        return self._to_seconds(self._total)

    @property
    def avg(self):
        """
        Returns average duration in seconds.
        """
        if self._count != 0:
            avg = self._to_seconds(self._total / self._count)
        else:
            avg = 0.0
        return avg

    @property
    def throughput(self):
        """
        Returns throughput in counts per seconds.
        """
        total_time = self.total
        if total_time != 0.0:
            throughput = round(
                float(self._count) / total_time, self._round_precision
            )
        else:
            throughput = 0.0
        return throughput

    def start(self):
        """
        Starts profiling. Increments count and starts the timer.
        """
        if self.is_running:
            raise RuntimeError("Profiler is already running")

        self.is_running = True
        self._count += 1
        self._start_time = time.time_ns()

    def stop(self):
        """
        Stops profiling. Stops timer and updates stats.
        """
        if not self.is_running:
            return

        run_time = time.time_ns() - self._start_time
        self._min = min(self._min, run_time)
        self._max = max(self._max, run_time)
        self._total += run_time
        self.is_running = False

    def to_dict(self):
        """
        Returns a dict representation of the stats.
        """
        return {
            "min": self.min,
            "max": self.max,
            "total": self.total,
            "average": self.avg,
            "count": self.count,
            "throughput": self.throughput,
        }

    def _to_seconds(self, val):
        """
        Converts val in nanoseconds to seconds and rounds it..
        """
        return round(float(val) / 1e9, self._round_precision)


class Tracker:
    """
    To track different ProfilerStats under one file
    NOTE: Should never need to be called directly. Call via
    `CurrentTracker.get_tracker`
    """

    def __init__(self, file_name):
        """
        Tracker instance to consume ProfilerStats
        """
        self.file_name = file_name
        self.ps_dict = {}
        self.data = {}
        self.depth_names = []

    def start(self, name):
        """
        Starts the profiler specified
        """
        ps = self.ps_dict.get(name, ProfileStats(name))
        if ps.is_running:
            raise NameError(
                f"Stat with name {name} cannot be started as it is already used"
                f"in Tracker collection"
            )
        parent = None
        parents = []
        if len(self.depth_names) > 0:
            parent = self.depth_names[-1]
            parents = self.data[parent][0] + [parent]
        self.data[name] = [parents, None]

        self.depth_names.append(name)
        self.ps_dict[name] = ps
        ps.start()

    def stop(self, name, ignore_not_running: bool = False):
        """
        Closes specified profiler and captures the result
        """
        ps = self.ps_dict.get(name)
        if ps is None:
            raise RuntimeError(
                f"Stat with name {name} cannot be stopped as it was never started"
            )
        if not ps.is_running:
            if ignore_not_running:
                return

            raise RuntimeError(
                f"Stat with name {name} cannot be stopped as it has already terminated"
            )

        ps.stop()
        self.data[name][1] = ps.total
        pos = self.depth_names.index(name)
        del self.depth_names[pos]
        self._save()

    def _save(self):
        """
        Saves the results from the profilers to a file
        """
        result = self._construct_result()
        with open(self.file_name, "w") as f:
            json.dump(result, f, indent=4)

    def _construct_result(self):
        result = {}
        for name, data in self.data.items():
            parents, time_taken = data
            sub_results = result
            for parent in parents:
                sub_results = sub_results[parent][1]
            sub_results[name] = [time_taken, {}]
        return result

    class Entry:
        """context manager class to wrap around the tracker's start and stop"""

        def __init__(self, tracker, name):
            self.tracker = tracker
            self.name = name

        def __enter__(self):
            self.tracker.start(self.name)

        def __exit__(self, *args):
            self.tracker.stop(self.name)

    def entry(self, name):
        """
        context manager wrapped around start and stop
        """
        return self.Entry(self, name)

    def get_stat_by_name(self, name):
        """
        Return a stat by name
        """
        if self.ps_dict.get(name) is None:
            raise NameError(
                f"Could not find a stat with name {name} in Tracker collection. "
                f"Valid stats include: {list(self.ps_dict.keys())}"
            )
        stat = self.data[name][1]
        if stat is None:
            raise RuntimeError(
                f"Stat with name {name} is not available as it has not yet terminated"
            )
        else:
            return stat


class CurrentTracker:
    """
    Global mechanism to retreive Tracker
    """

    _CURRENT_TRACKERS = {}

    @staticmethod
    def get_tracker(key, file_name):
        """
        Creates or returns an existing tracker
        key: lookup key to find the tracker
        file_name: In case the tracker doesn't exist, file_name to be
            used to create the tracker
        """
        if key not in CurrentTracker._CURRENT_TRACKERS:
            assert (
                file_name
            ), f"Invalid tracker: {key}. file_name `{file_name}` should not be None or empty string"
            CurrentTracker._CURRENT_TRACKERS[key] = Tracker(file_name=file_name)
        else:
            if (
                file_name
                and file_name != CurrentTracker._CURRENT_TRACKERS[key].file_name
            ):
                logging.warning(
                    f"tracker {key} already exists with file_name "
                    f"{CurrentTracker._CURRENT_TRACKERS[key].file_name} so cannot "
                    f"use {file_name}"
                )
        return CurrentTracker._CURRENT_TRACKERS[key]


@contextmanager
def limit_mp_threads():
    """Turn off threadings parameters for multiprocessing situations"""
    thread_reductions = {
        'OPENBLAS_NUM_THREADS': '1',
        'OMP_NUM_THREADS': '1',
        'XLA_THREAD_POOL_SIZE': '1',
        'XLA_IO_THREAD_POOL_SIZE': '1',
    }
    original_env_values = {}
    additional_env_keys = []
    for key in thread_reductions:
        value = os.environ.get(key, None)
        if value is not None:
            original_env_values[key] = value
        else:
            additional_env_keys.append(key)
    try:
        os.environ.update(thread_reductions)
        yield
    finally:
        os.environ.update(original_env_values)
        for key in additional_env_keys:
            os.environ.unsetenv(key)


def pip_list() -> Dict[str, str]:
    """Returns formatted output from pip list to capture current env"""
    args = [sys.executable, "-m", "pip", "list", "--format", "freeze"]
    p = subprocess.run(args, check=True, capture_output=True)
    freeze_outputs = p.stdout.decode().split("\n")
    dependencies = dict(
        package_requirement.split('==')
        for package_requirement in freeze_outputs
        if '==' in package_requirement
    )
    # TODO: Improve filtering (SW-88646)
    # TODO: Support alternative torch dependencies (SW-88648)
    for dep in get_deps():
        if dep in dependencies:
            del dependencies[dep]

    return dependencies


def version_check(external_component: str, ext_version: str, ext_githash: str):
    """Validate server version info"""
    if __githash__ == ext_githash:
        # No matter the version strings, its the same build so its compatible.
        return
    # Build mismatch of some kind.
    server_public = ext_version.split("-")[0]
    client_public = __version__.split("+")[0]
    if (
        client_public == server_public
        or server_public == "0.0.0"
        or client_public == "0.0.0"
    ):
        # Internal build mismatch
        error_msg = (
            f"Client software is version {__version__} on {__githash__} but "
            f"{external_component} version is {ext_version} on {ext_githash}."
        )
    else:
        # Release version mismatch
        error_msg = (
            f"{external_component} has version: {server_public} but client "
            f"has {client_public}.\nIn order to use this cluster, you must "
            f"install {server_public} of the client.\n"
        )
    raise ApplianceVersionError(error_msg)


@lru_cache(maxsize=1)
def is_cerebras_available():
    """Simple check for availability of internal cerebras package"""
    return find_spec("cerebras") is not None
