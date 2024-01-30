from typing import Dict, List
from time import sleep

from components import BaseComponent
from models import Trajectory, TrajectoryMode
from utils import BBox
from models import Input
from models import Output
from models import Frame


class BaseTrackeComponent(BaseComponent):
    def __init__(self, name: str, trajectory_mode: int = TrajectoryMode.CENTER):
        super().__init__(name=name)
        self._TRAJECTORIES_BUFFER: List[Trajectory] = []
        self._trajectory_mode: int = trajectory_mode
        self._inputs["detections"] = Input()
        self._outputs["trajectories"] = Output()
        self._outputs["lost_trajectories"] = Output()

    def track(self, detection: BBox) -> List[Trajectory]:
        ...

    def do(self):
        detections: List[BBox] = self._inputs["detections"].get()
        frame: Frame = self._inputs["frames"].get()

        if detections is not None:
            for detection in detections:
                self._TRAJECTORIES_BUFFER = self.track(detection)

            if self._outputs["trajectories"].is_linked():
                self.outputs["trajectories"].set(self._TRAJECTORIES_BUFFER)

            if self._outputs["lost_trajectories"].is_linked():
                lost_trajectories = []
                for trajectory in self._TRAJECTORIES_BUFFER:
                    if trajectory.is_lost():
                        lost_trajectories.append(trajectory)
                self.outputs["lost_trajectories"].set(lost_trajectories)

            if self._outputs["frames"].is_linked() and frame is not None:
                [
                    trajectory.draw(frame.image)
                    for trajectory in self._TRAJECTORIES_BUFFER
                ]
                self.outputs["frames"].set(frame)

            [
                self._TRAJECTORIES_BUFFER.pop(index)
                for index, trajectory in enumerate(self._TRAJECTORIES_BUFFER)
                if trajectory.is_lost()
            ]
