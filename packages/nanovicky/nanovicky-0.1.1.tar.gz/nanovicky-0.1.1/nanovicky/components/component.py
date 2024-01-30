from datetime import datetime, timedelta
from typing import Dict

from utils import logger


class Benchmark:
    def __init__(self, label: str = None) -> None:
        self._last_fps_time: datetime = datetime.now()
        self._begin_time: datetime = None
        self._iterations: int = 0
        self._last_n_iterations: int = 0
        self._PERFORMANCE_BUFFER: Dict[
            datetime, datetime
        ] = {}  # List of execution time
        self._FPS_BUFER: Dict[datetime, int] = {}
        self._label: str = label

    def set_begin(self):
        """Set the begin time of the Benchmarker"""
        self._begin_time = datetime.now()
        return self

    def compute_fps(self):
        current_time: datetime = datetime.now()
        if current_time - self._last_fps_time > timedelta(seconds=1):
            self._FPS_BUFFER = {}
            self._FPS_BUFER[current_time] = self._last_n_iterations
            self._last_n_iterations = 0
            self._last_fps_time = current_time

    def set_end(self):
        """Set the end time of the benchmarker"""
        end_time: datetime = datetime.now()

        # Temporary, empty buffers before assigning values
        self._PERFORMANCE_BUFFER = {}
        self._PERFORMANCE_BUFFER[end_time] = (end_time - self._begin_time).microseconds
        self.compute_fps()

        self._iterations = self._iterations + 1
        self._last_n_iterations = self._last_n_iterations + 1
        return self

    def mean_performances(self) -> float:
        return float(
            sum(self._PERFORMANCE_BUFFER.values())
            / len(self._PERFORMANCE_BUFFER.values())
        )

    def max_performance(self):
        return max(self._PERFORMANCE_BUFFER.values())

    def min_performance(self):
        return min(self._PERFORMANCE_BUFFER.values())

    def report(self):
        return {
            "label": self._label,
            "iterations": self._iterations,
            "fps": list(self._FPS_BUFER.values())[-1]
            if self._FPS_BUFER.values()
            else None,
            "performance": list(self._PERFORMANCE_BUFFER.values())[-1]
            if self._PERFORMANCE_BUFFER.values()
            else None,
        }


class Component:
    def __init__(self, name: str = None):
        self._name = name
        self.logger = logger.create_logger(name=self._name)
        # benchmark
        self._perf_analysis: bool = False
        self._benchmarker: Benchmark = Benchmark(self._name)

    def log_message(self, message: str):
        return f"{self._name} - {message}"

    @property
    def name(self):
        return self._name

    def __str__(self):
        return self._name
