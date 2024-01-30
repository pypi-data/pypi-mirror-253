from datetime import datetime, timedelta

import cv2 as opencv

from nanovicky.components.base_component import BaseComponent
from nanovicky.models.frame import Frame


class BenchmarkComponent(BaseComponent):
    def __init__(self, name: str):
        super().__init__(name=name)
        self._mean_fps: int = None
        self._last_second = None
        self._frame_processed: int = None
        self._last_frame_processed: int = None

    def initiate(self):
        self._last_second = datetime.now()
        self._frame_processed = 0

    def do(self):
        frame: Frame = self._inputs["frames"].get()
        if frame is not None:
            self._frame_processed = self._frame_processed + 1

            if datetime.now() - self._last_second > timedelta(seconds=1):
                # Assign the number of frame processed to the min fps
                self._mean_fps = (
                    int((self._last_frame_processed + self._frame_processed) / 2)
                    if self._last_frame_processed is not None
                    else self._frame_processed
                )

                # Reset last second and frame processed
                self._last_second = datetime.now()
                self._frame_processed = 0
                self._last_frame_processed = self._mean_fps

            if self._outputs["frames"].is_linked():
                opencv.putText(
                    frame.image,
                    f"FPS : {self._mean_fps}",
                    (10, 15),
                    opencv.FONT_HERSHEY_PLAIN,
                    1.0,
                    (255, 0, 255),
                    2,
                )
                opencv.putText(
                    frame.image,
                    f"Res : {frame.image.shape[:2]}",
                    (100, 15),
                    opencv.FONT_HERSHEY_PLAIN,
                    1.0,
                    (150, 255, 0),
                    2,
                )
                self._outputs["frames"].set(frame)
