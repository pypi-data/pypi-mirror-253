from time import sleep
from threading import Thread
from components import BaseComponent


class ThreadComponent:
    def __init__(self, component: BaseComponent):
        self._thread = Thread(target=self._run, daemon=True)
        self._live: bool = True
        self._component: BaseComponent = component

        self._started: bool = False  # Allow the program to know if a join is to performed at the end of the program or not

    def begin(self):
        self._thread.start()
        self._started = True
        return self

    def _run(self):
        while self._live:
            self._component.execute()

    def end(self):
        self._component.stop()
        self._live = False
        if self._started:
            self._thread.join()
        return self

    @property
    def component(self):
        return self._component

    def is_alive(self):
        return self._live

    def __str__(self) -> str:
        return self._component.name
