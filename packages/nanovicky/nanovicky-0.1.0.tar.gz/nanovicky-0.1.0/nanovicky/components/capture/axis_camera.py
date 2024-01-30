from typing import Tuple, Dict
import logging

from components import CameraComponent


class AXISCameraComponent(CameraComponent):
    def __init__(
        self,
        name: str,
        host: str,
        mode: str = "MJPG",
        username: str = None,
        password: str = None,
        resolution: Tuple[int, int] = (640, 360),
        scale: float = 1,
    ):
        self._host: str = host
        self._mode: str = mode
        self._username: str = username
        self._password: str = password

        url: Dict[str, str] = {
            "H264": f"rtsp://{self._username}:{self._password}@{self._host}:554/axis-media/media.amp?videocodec=h264&resolution={resolution[0]}x{resolution[1]}",
            "MJPG": f"http://{self._username}:{self._password}@{self._host}/mjpg/video.mjpg?resolution={resolution[0]}x{resolution[1]}",
        }

        self._camera_url = url[mode]
        super().__init__(
            channel=self._camera_url, resolution=resolution, scale=scale, name=name
        )
