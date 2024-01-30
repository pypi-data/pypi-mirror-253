from os import path
from time import sleep
from typing import List, Tuple
from datetime import datetime, timedelta

import cv2 as opencv

from models import Frame
from components import BaseCaptureComponent


class VideoComponent(BaseCaptureComponent):
    def __init__(
        self,
        name: str,
        channel: str,
        frame_interval: Tuple[int, int] = (0, None),
        scale: float = 1.0,
        first_timestamp: int = datetime.now().timestamp(),
        fps: int = 25,
    ):
        super().__init__(
            channel=channel, first_timestamp=first_timestamp, scale=scale, name=name
        )
        self._fps: int = fps
        self._frame_interval: Tuple[int, int] = frame_interval
        self._total_frame_count: int = 0
        self._index: int = frame_interval[0]

    def initiate(self):
        self._total_frame_count = self._camera.get(opencv.CAP_PROP_FRAME_COUNT)

    def do(self):
        result, image = self._camera.read()
        if result:
            final_frame = opencv.resize(
                image,
                (
                    int(image.shape[1] * self._scale),
                    int(image.shape[0] * self._scale),
                ),
                interpolation=opencv.INTER_AREA,
            )

            print(f"Frame : {self._index} / {self._total_frame_count}")

            # opencv.putText(final_frame, str(self._iterations), (10, 10), opencv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
            if self._outputs["frames"].is_linked():
                self._ellapsed_time = self._ellapsed_time + timedelta(seconds=1 / 15)

                new_frame: Frame = Frame(final_frame, self._index, self._ellapsed_time)

                opencv.putText(
                    new_frame.image,
                    f"{self._ellapsed_time}",
                    (10, 10),
                    opencv.FONT_HERSHEY_PLAIN,
                    1,
                    (255, 255, 255),
                    1,
                )
                #                opencv.putText(new_frame.image, f"{new_frame._index} / {self._total_frame_count}", (300, 10), opencv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
                self._outputs["frames"].set(new_frame)

            self._index += 1

        if (
            self._frame_interval[1] is not None
            and self._index == self._frame_interval[1]
        ):
            print(f"We've reached the {self._frame_interval[1]} milestones")
            self.stop()
