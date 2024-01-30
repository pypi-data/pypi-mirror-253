from typing import Dict

from components import BaseComponent
from models import Input, FrameInput
from models import Output, FrameOutput
from models import Frame


class BaseDetectorComponent(BaseComponent):
    def __init__(self, name: str):
        super().__init__(name=name)

        self._inputs: Dict[str, Input] = {"frames": FrameInput()}
        self._outputs: Dict[str, Output] = {
            "frames": FrameOutput(),
            "detections": Output(),
        }
