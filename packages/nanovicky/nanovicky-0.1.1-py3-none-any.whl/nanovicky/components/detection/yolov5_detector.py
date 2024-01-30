from typing import List

import cv2 as opencv
import numpy as np
import torch

from components import BaseDetectorComponent
from models import Frame
from models import Detection
from utils import BBox
from utils import Point


class YoloV5DetectorComponent(BaseDetectorComponent):
    def __init__(self, name: str, model_path: str):
        super().__init__(name=name)
        self._model_path: str = model_path
        self._model = torch.hub.load(
            "/home/anatole/Projets/ocular/lab/yolov5/",
            "custom",
            path=self._model_path,
            source="local",
        )

    def do(self):
        frame: Frame = self._inputs["frames"].get()

        if frame is not None:
            image = [frame.image]
            predictions = self._model(image)

            results: List = predictions.xyxy[0].tolist()

            detections: List[Detection] = [
                Detection(BBox(Point(int(x1), int(y1)), Point(int(x2), int(y2))))
                for x1, y1, x2, y2, _, _ in results
            ]

            if self._outputs["frames"].is_linked():
                self._outputs["frames"].set(frame)

            if self._outputs["detections"].is_linked():
                self._outputs["detections"].set(detections)
