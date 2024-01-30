import cv2 as opencv

from cameras.models import Camera
import logging
from utils import NoCameraAvailable
from typing import Tuple

def get_camera(channel: int, logger: logging.Logger, name: str, resolution: Tuple[int, int]) -> opencv.VideoCapture:
        camera = opencv.VideoCapture(channel)

        # no camera on given channel so checking others channel on devices
        if not camera.isOpened():
            camera_array = get_all_available_camera()
            if len(camera_array) <= 0:
                logger.critical(f"{name} no camera found, channel: {channel}")
                raise NoCameraAvailable(f"{name} no camera found, channel: {channel}")

            camera = opencv.VideoCapture(camera_array[0])
            logger.warning(
                f"camera channel {channel} not found, switch on channel {camera_array[0]}"
            )

        camera.set(opencv.CAP_PROP_FRAME_WIDTH, resolution[0])
        camera.set(opencv.CAP_PROP_FRAME_HEIGHT, resolution[1])
        return camera

def get_all_available_camera():
    index = 0
    arr = []
    for index in range(0, 14):
        cap = opencv.VideoCapture(index)
        if not cap.read()[0]:
            continue
        arr.append(index)
        cap.release()
    return arr


class UsbCameraComponent(Camera):
    def __init__(self, channel: int, name: str, resolution: Tuple[int, int], scale: float):
            super().__init__(name=name, channel=channel, resolution=resolution, scale=scale)
            self.camera: Camera = get_camera(channel=channel, logger=self.logger, name=name, resolution=resolution)
            self.framerate: int = int(self.camera.get(opencv.CAP_PROP_FPS))
        
    def read(self):
        super().read()
        result, image = self.camera.read()
        if result:
            return image
        return None
