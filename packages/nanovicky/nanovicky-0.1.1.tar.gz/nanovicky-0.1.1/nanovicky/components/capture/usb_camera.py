from typing import Tuple

from components import CameraComponent


class USBCameraComponent(CameraComponent):
    def __init__(
        self,
        name: str,
        channel: int = 0,
        resolution: Tuple[int, int] = (680, 480),
        scale: float = 1,
    ):
        super().__init__(channel=channel, resolution=resolution, scale=scale, name=name)
