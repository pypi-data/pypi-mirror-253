from datetime import datetime, timedelta
from typing import List, Dict

import cv2 as opencv
import numpy as np

from utils import Drawables
from utils import Point
from utils import Detection
from utils import Color, Colors
from components import (
    GENDER_AGE_VALUES,
)


TIME_TO_TRAJECTORY_LOSS = timedelta(seconds=2)


class TrajectoryMode:
    TOP: int = 0
    CENTER: int = 1
    BOTTOM: int = 2


class Trajectory(Drawables):
    def __init__(
        self,
        trajectory_mode: int = TrajectoryMode.CENTER,
        offset: int = 20,
        timestamp: datetime = datetime.now(),
    ) -> None:
        self._points: List[Point] = []
        self._last_update: datetime = timestamp
        self._last_detection: Detection = None
        self._trajectory_mode: int = trajectory_mode
        self._offset: int = offset
        self._detections: Dict[int, int] = {}
        self._trajectory_detections: List[Detection] = []

    def is_lost(self) -> bool:
        return datetime.now() - self._last_update > TIME_TO_TRAJECTORY_LOSS

    def update(self, detection: Detection):
        self._trajectory_detections.append(detection)
        self._points.append(
            {
                TrajectoryMode.TOP: detection._bbox.top() + Point(0, self._offset),
                TrajectoryMode.CENTER: detection._bbox.center(),
                TrajectoryMode.BOTTOM: detection._bbox.bottom()
                + Point(0, -self._offset),
            }[self._trajectory_mode]
        )
        self._last_detection = detection
        self._last_update = datetime.now()

        if detection._object in self._detections.keys():
            self._detections[detection._object] += 1
        else:
            self._detections[detection._object] = 1

        return self

    def draw(self, image, color: Color = Colors.RED) -> Color:
        _, _, label, color = GENDER_AGE_VALUES[self.max_score_detection()]
        opencv.putText(
            image,
            label,
            self._last_detection._bbox.pt1.value(),
            opencv.FONT_HERSHEY_PLAIN,
            2.0,
            color.cv_color(),
            3,
        )
        self._last_detection._bbox.draw(image, color)
        opencv.polylines(image, self.curve, False, color.cv_color(), 2)

    def max_score_detection(self) -> int:
        max_score: int = 0
        gender_age: int = None

        for gender_age_index, score in self._detections.items():
            gender_age = gender_age_index if max_score < score else gender_age
            max_score = score if max_score < score else max_score

        return gender_age

    def direction(self) -> int:
        return int(self.points[-1].y < self.points[0].y)

    @property
    def points(self):
        return self._points

    @property
    def curve(self):
        points = self._points
        # points = [points[i] for i in range(0, len(points), 3)]
        return [
            np.array([point.value() for point in points], np.int32).reshape((-1, 1, 2))
        ]

    @property
    def bbox(self):
        return self._last_detection._bbox
