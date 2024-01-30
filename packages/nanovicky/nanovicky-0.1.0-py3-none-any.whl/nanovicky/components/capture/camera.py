from typing import Tuple

import cv2 as opencv
from components import BaseCaptureComponent


class CameraComponent(BaseCaptureComponent):
    def __init__(
        self,
        channel: int,
        name: str,
        resolution: Tuple[int, int] = (640, 480),
        scale: float = 1.0,
    ):
        super().__init__(channel=channel, scale=scale, name=name)
        self._resolution: Tuple[int, int] = resolution

    def initiate(self):
        super().initiate()
        self._camera.set(opencv.CAP_PROP_FRAME_WIDTH, self._resolution[0])
        self._camera.set(opencv.CAP_PROP_FRAME_HEIGHT, self._resolution[1])
