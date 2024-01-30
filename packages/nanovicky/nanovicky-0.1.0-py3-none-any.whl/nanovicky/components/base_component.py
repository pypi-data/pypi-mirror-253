import logging
from typing import Dict
from time import sleep

from components import Component
from models import Input
from models import Output


class ExecutionErrorException(Exception):
    ...


class HamperedExecutionException(Warning):
    ...


class ExecutionMode:
    NORMAL: int = 0
    BENCHMARK: int = 1


class BaseComponent(Component):
    def __init__(self, execution_mode: int = ExecutionMode.BENCHMARK, name: str = None):
        super().__init__(name=name)
        self._inputs: Dict[str, Input] = {"frames": Input()}
        self._outputs: Dict[str, Output] = {"frames": Output()}
        self._enabled: bool = True
        self._running: bool = False

        # Execution function
        self._execution_mode: int = execution_mode
        self._main_execution = [self.do, self.do_benchmark]

    def start(self):
        self._running = True
        return self

    def stop(self):
        self.pause()
        self._running = False
        return self

    def pause(self):
        self._enabled = False
        return self

    def run(self):
        self._main_execution[self._execution_mode]()

    def _execution(self):
        self.initiate()

        while self._running:
            try:
                self.run() if self._enabled else sleep(0.1)
            except StopIteration:
                sleep(0.1)
            except ExecutionErrorException as error:
                logging.error(self.log_message(f"{error}"))
            except HamperedExecutionException:
                sleep(0.1)

        self.terminate()

    def execute(self):
        self._execution()

    def initiate(self):
        ...

    def do(self):
        ...

    def do_benchmark(self):
        self._benchmarker.set_begin()
        self.do()
        self._benchmarker.set_end()

    def terminate(self):
        ...

    @property
    def outputs(self):
        return self._outputs

    @property
    def inputs(self):
        return self._inputs

    def set_mode(self, execution_mode: int):
        self._execution_mode = execution_mode
        return self

    def __str__(self):
        return self._name
