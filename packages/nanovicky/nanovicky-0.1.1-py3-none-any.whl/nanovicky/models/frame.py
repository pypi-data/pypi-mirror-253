from datetime import datetime
from typing import Dict, List
import base64

import cv2 as opencv
from numpy import ndarray
import numpy
from PIL import Image
import io


def create_frame_from64(base64_string: str, timestamp: datetime):
    return Frame(
        opencv.cvtColor(
            numpy.array(Image.open(io.BytesIO(base64.b64decode(base64_string)))),
            opencv.COLOR_BGR2RGB,
        ),
        0,
        timestamp=timestamp,
    )


class Frame:
    def __init__(
        self, image: ndarray, index: int, timestamp: datetime = None, elements=[]
    ):
        self._image: ndarray = image
        self._timestamp = datetime.now() if timestamp is None else timestamp
        self._elements: List = elements
        self._index: int = index

    def set_elements(self, elements):
        if elements is not None:
            elements = elements if isinstance(elements, List) else [elements]
            self._elements = self._elements + elements
        return self

    def draw(self):
        [element.draw(self._image) for element in self._elements]

    def to64(self, format: str = "jpg") -> bytes:
        """Generates a base64 string image for it to be send in requests.

        Args:
            format (str, optional): The encoding format. Defaults to 'jpg'.

        Returns:
            bytes: The base 64 image
        """

        return base64.b64encode(opencv.imencode(f".{format}", self._image)[1])

    @property
    def image(self):
        return self._image


class FrameTest:
    def __init__(self, index: int, capture, timestamp=None, elements=None) -> None:
        self._index = index
        self._timestamp = datetime.now() if timestamp is None else timestamp
        self._elements = elements
        self._capture: opencv.VideoCapture = capture

    def image(self):
        # get total number of frames
        totalFrames = self._capture.get(opencv.CAP_PROP_FRAME_COUNT)

        # check for valid frame number
        if self._index >= 0 & self._index <= totalFrames:
            # set frame position
            opencv.set(opencv.CAP_PROP_POS_FRAMES, self._index)
