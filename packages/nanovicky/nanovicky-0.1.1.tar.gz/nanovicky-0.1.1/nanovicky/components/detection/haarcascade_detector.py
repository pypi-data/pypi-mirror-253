from typing import List
from pathlib import Path

import cv2 as opencv

from components import BaseDetectorComponent
from models import Frame
from utils import BBox
from detection import Detection
from utils import Point


class HaarCascadeDetectorComponent(BaseDetectorComponent):
    def __init__(self, name: str, detector_path: Path):
        super().__init__(name=name)
        self._detector_path: Path = detector_path
        self.body_classifier = opencv.CascadeClassifier(
            str(self._detector_path.absolute())
        )

    def do(self):
        frame: Frame = self.inputs["frames"].get()

        if frame is not None:
            bboxes: List[Detection] = [
                BBox(
                    Point(detection[0], detection[1]),
                    Point(detection[0] + detection[2], detection[1] + detection[3]),
                )
                for detection in self.body_classifier.detectMultiScale(
                    frame.image,
                    scaleFactor=1.05,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags=opencv.CASCADE_SCALE_IMAGE,
                )
            ]

            if self._outputs["frames"].is_linked():
                frame.set_elements(bboxes)
                self._outputs["frames"].set(frame)

            if self._outputs["detections"].is_linked():
                self._outputs["detections"].set(bboxes)
