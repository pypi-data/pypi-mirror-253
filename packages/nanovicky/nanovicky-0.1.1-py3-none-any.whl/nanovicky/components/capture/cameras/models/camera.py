from components import BaseComponent, ExecutionMode
from typing import Tuple

class Camera(BaseComponent): 
    def __init__(self, name: str, channel: int, resolution: Tuple[int, int], scale: float):
        super().__init__(name=name)
        
        self.channel: int = channel
        self.resolution: Tuple[int, int] = resolution
        self.scale: float = scale
        self.framerate: int

    def read(self):
        ...
