from time import sleep
from datetime import datetime
from typing import Dict
import cv2 as opencv

from models import Frame
from models import FrameInput
from components import BaseComponent


class DisplayerComponent(BaseComponent):
    def __init__(self, name: str):
        super().__init__(name=name)
        self._inputs = {"frames": FrameInput()}

    def initiate(self):
        super().initiate()
        opencv.namedWindow(self._name, opencv.WINDOW_NORMAL)

    def do(self):
        frame: Frame = self._inputs["frames"].get()

        if frame is not None:
            opencv.imshow(self._name, frame.image)

        if opencv.waitKey(30) == 27:
            self.pause()

    def terminate(self):
        super().terminate()
        opencv.destroyWindow(self._name)
