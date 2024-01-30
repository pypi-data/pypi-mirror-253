from typing import List, Tuple, Dict

import numpy as np
import cv2 as opencv

from models.data import Data
from models.detection import Detection
from models.frame import Frame
from components.detection.base_detector import BaseDetectorComponent
from .helper.edgetpumodel import EdgeTPUModel
from .helper.utils import get_image_tensor
from utils.shapes.bbox import BBox
from utils.shapes.shapes import Point
from utils.drawing.color import Color


GENDER_AGE_VALUES: Dict[int, Tuple[int, int, str, Color]] = {
    0: (2, 1, "woman_0-12", Color(255, 0, 0)),
    1: (2, 2, "woman_13-18", Color(255, 51, 0)),
    2: (2, 3, "woman_19-30", Color(255, 103, 0)),
    3: (2, 4, "woman_31-50", Color(255, 155, 0)),
    4: (2, 5, "woman_+51", Color(255, 255, 0)),
    5: (1, 1, "man_0-12", Color(0, 0, 255)),
    6: (1, 2, "man_13-18", Color(0, 51, 255)),
    7: (1, 3, "man_19-30", Color(0, 103, 255)),
    8: (1, 4, "man_31-50", Color(0, 155, 255)),
    9: (1, 5, "man_+51", Color(0, 255, 255)),
}


class YoloEdgetpuDetectorComponent(BaseDetectorComponent):
    def __init__(
        self,
        weights_path: str,
        labels_path: str,
        confidence_threshold: float = 0.25,
        iou_threshold: float = 0.45,
        name: str = "YoloEdgetpuDetectorComponent",
    ):
        super().__init__(name=name)
        self._weights_path: str = weights_path
        self._labels_path: str = labels_path
        self._confidence_threshold: float = confidence_threshold
        self._iou_threshold: float = iou_threshold
        self._model: EdgeTPUModel = EdgeTPUModel(
            self._weights_path,
            self._labels_path,
            self._confidence_threshold,
            self._iou_threshold,
        )
        self._input_size = self._model.get_image_size()

    def initiate(self):
        return super().initiate()

    def do(self):
        frame: Frame = self._inputs["frames"].get()

        if frame is not None:
            full_image, net_image, pad = get_image_tensor(
                frame.image, self._input_size[0]
            )
            pred: np.ndarray = self._model.forward(net_image)

            # Returns a list of Tuple, with the scaled detection, and the class associated to it
            scaled_detection: List[
                Tuple[List[int], int]
            ] = self._model.process_predictions(pred[0], full_image, pad)

            detections: List[Detection] = []
            for result in scaled_detection:
                x1, y1, x2, y2 = result[0]
                gender, age, _, _ = GENDER_AGE_VALUES[result[1]]

                bbox: BBox = BBox(Point(int(x1), int(y1)), Point(int(x2), int(y2)))
                obj = result[1]
                detections.append(Detection(bbox, frame._timestamp, obj))

            if self._outputs["frames"].is_linked():
                opencv.putText(
                    full_image,
                    f"FPS : {list(self._benchmarker._FPS_BUFER.values())[-1] if self._benchmarker._FPS_BUFER.values() else None}",
                    (50, 50),
                    opencv.FONT_HERSHEY_COMPLEX,
                    1.0,
                    (255, 0, 255),
                )
                self._outputs["frames"].set(
                    Frame(full_image, frame._index, frame._timestamp)
                )

            if self._outputs["detections"].is_linked():
                self._outputs["detections"].set(detections)
