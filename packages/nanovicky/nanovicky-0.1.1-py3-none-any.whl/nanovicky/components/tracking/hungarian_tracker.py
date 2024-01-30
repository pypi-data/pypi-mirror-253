from typing import List, Generator

from components import BaseTrackeComponent
from helper import get_iou
from detection import Detection
from models import Trajectory, TrajectoryMode


MIN_REQUIRED_IOU: float = 0.2


class HungarianTrackerComponent(BaseTrackeComponent):
    def __init__(
        self,
        name: str,
        trajectory_mode: int = TrajectoryMode.TOP,
        min_required_iou: float = 0.2,
    ):
        super().__init__(trajectory_mode=trajectory_mode, name=name)
        self._min_required_iou: float = min_required_iou

    def track(self, detection: Detection) -> List[Trajectory]:
        # Buffer value
        max_value_index: int = 0
        max_ious: int = 0.0

        # Check if trajectories where already registered
        if self._TRAJECTORIES_BUFFER:
            ious: List[float] = [
                get_iou(detection._bbox, trajectory.bbox)
                for trajectory in self._TRAJECTORIES_BUFFER
            ]
            max_ious = max(ious)
            max_value_index: int = ious.index(max_ious)

        # Check if a result is above mix required_value
        if max_ious > self._min_required_iou:
            self._TRAJECTORIES_BUFFER[max_value_index].update(detection)
            return self._TRAJECTORIES_BUFFER

        self._TRAJECTORIES_BUFFER.append(
            Trajectory(trajectory_mode=self._trajectory_mode).update(detection)
        )

        return self._TRAJECTORIES_BUFFER
