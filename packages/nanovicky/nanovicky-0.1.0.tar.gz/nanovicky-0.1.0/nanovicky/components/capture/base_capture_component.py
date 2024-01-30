from datetime import datetime, timedelta
from typing import Dict
import cv2 as opencv

from components import BaseComponent
from models import Frame
from models import FrameOutput

from cameras.models import Camera

from utils import NoCameraAvailable
import logging


def get_camera(channel: int, name: str, logger: logging.Logger) -> opencv.VideoCapture:
    camera = opencv.VideoCapture(channel)
    if not camera.isOpened():
        camera_array = get_all_available_camera()
        if len(camera_array) <= 0:
            logger.critical(f"{name} no camera found, channel: {channel}")
            raise NoCameraAvailable(f"{name} no camera found, channel: {channel}")

        camera = opencv.VideoCapture(camera_array[0])
        logger.warning(
            f"camera channel {channel} not found, switch on channel {camera_array[0]}"
        )
    return camera


def get_all_available_camera():
    index = 0
    arr = []
    for index in range(0, 14):
        cap = opencv.VideoCapture(index)
        if not cap.read()[0]:
            continue
        arr.append(index)
        cap.release()
    return arr


class BaseCaptureComponent(BaseComponent):
    def __init__(
        self,
        name: str,
        camera: Camera,
        scale: float = 1.0,
        first_timestamp: float = datetime.now().timestamp(),
        
    ):
        super().__init__(name=name)
        # WARNING SI PAS CHANNEK DEFAULT
        self._first_timestamp: float = first_timestamp
        self._scale: float = scale
        self._camera: Camera = camera
        self._iterations: int = 0
        self._ellapsed_time: datetime = datetime.fromtimestamp(self._first_timestamp)
        self.current_frame: Frame = None

    def initiate(self):
        return super().initiate()

    def do(self):
        super().do()
        image = self._camera.read()

        if image is not None:
            final_frame = opencv.resize(
                image,
                (
                    int(image.shape[1] * self._scale),
                    int(image.shape[0] * self._scale),
                ),
                interpolation=opencv.INTER_AREA,
            )
            # opencv.putText(final_frame, str(self._iterations), (10, 10), opencv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

            if self._outputs["frames"].is_linked():
                self._ellapsed_time: datetime = self._ellapsed_time + timedelta(
                    seconds=1 / self._camera.framerate
                )

                new_frame: Frame = Frame(
                    final_frame, self._iterations, self._ellapsed_time
                )

                # opencv.putText(new_frame.image, f"{datetime.now()}", (10, 10), opencv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
                self.current_frame = new_frame
                self._outputs["frames"].set(self.current_frame)

            self._iterations += 1

    def terminate(self):
        super().terminate()
        self._camera.release()

    def ellapsed_time(self) -> int:
        return self._first_timestamp

    def get(self):
        while True:
            try:
                yield self._outputs["frames"]
            except KeyError:
                yield None
