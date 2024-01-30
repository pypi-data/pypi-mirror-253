from typing import List, Tuple
from random import randint
from datetime import datetime, timezone

import cv2 as opencv

from models import Detection
from components import BaseComponent
from models import Input
from models import Output
from utils import Line
from models import Trajectory
from helper import intersects
from models import Frame
from utils import Color
from components import (
    GENDER_AGE_VALUES,
)


CROSSING_DIRECTION = [2, 1]


class Direction:
    UP: int = 0
    DOWN: int = 1


class LineCrossingComponent(BaseComponent):
    def __init__(self, name: str, line: Line):
        super().__init__(name=name)
        self._inputs["trajectories"] = Input()
        self._outputs["counting"] = Output()
        self._outputs["eval"] = Output()
        self._line: Line = line
        self._counting_up: int = 0
        self._counting_down: int = 0

    def do(self):
        frame: Frame = self._inputs["frames"].get()
        trajectories: List[Trajectory] = self._inputs["trajectories"].get()

        counting_data = []
        eval_data = []

        if trajectories is not None:
            for trajectory in trajectories:
                # Examine all trajectories and check if they are crossing the line
                for pt1, pt2 in zip(self._line.points, self._line.points[1:]):
                    crossing_direction, crossing_detection = self.check_trajectory(
                        trajectory, (pt1.value(), pt2.value())
                    )

                    if crossing_direction is not None:
                        crossing_bbox = crossing_detection._bbox
                        gender, age, _, _ = GENDER_AGE_VALUES[
                            trajectory.max_score_detection()
                        ]

                        data = {
                            "timestamp": crossing_detection._timestamp.timestamp(),
                            "gender": gender,
                            "age": age,
                            "directionPass": CROSSING_DIRECTION[crossing_direction],
                        }

                        counting_data.append(data)

                        if crossing_direction == Direction.DOWN:
                            if self._outputs["eval"].is_linked():
                                data.update(
                                    {
                                        "x": crossing_bbox.pt1.x,
                                        "y": crossing_bbox.pt1.y,
                                        "width": crossing_bbox.width,
                                        "height": crossing_bbox.height,
                                    }
                                )
                                eval_data.append(data)

                            self._counting_down = self._counting_down + 1
                        elif crossing_direction == Direction.UP:
                            self._counting_up = self._counting_up + 1

        if self._outputs["counting"].is_linked():
            self._outputs["counting"].set(counting_data)

        if self._outputs["eval"].is_linked():
            self._outputs["eval"].set(eval_data)

        if self._outputs["frames"].is_linked() and frame is not None:
            self._line.draw(frame.image)
            opencv.putText(
                frame.image,
                f"Count UP : {self._counting_up}",
                (10, 40),
                opencv.FONT_HERSHEY_PLAIN,
                2.0,
                (220, 220, 220),
                2,
            )
            opencv.putText(
                frame.image,
                f"Count DOWN : {self._counting_down}",
                (10, 80),
                opencv.FONT_HERSHEY_PLAIN,
                2.0,
                (220, 220, 220),
                2,
            )
            self._outputs["frames"].set(frame)

    def is_intersecting(self, trajectory: Trajectory, segment):
        for point, point1 in zip(trajectory.points, trajectory.points[1:]):
            if intersects((point.value(), point1.value()), segment):
                return True
        return False

    def check_trajectory(
        self, trajectory: Trajectory, segment
    ) -> Tuple[Direction, Detection]:
        final_detection: Detection = None
        final_direction: Direction = None

        index: int = 0

        for point, point1 in zip(trajectory.points, trajectory.points[1:]):
            if intersects((point.value(), point1.value()), segment):
                final_direction = Direction.DOWN if point.y < point1.y else Direction.UP
                final_detection = trajectory._trajectory_detections[index]
            index += 1

        return final_direction, final_detection
