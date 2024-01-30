from cameras.models import Camera
from utils import NoCameraAvailable
import logging
from typing import Tuple
from picamera2 import Picamera2
import cv2 as opencv

def get_camera(channel: int, name: str, logger: logging.Logger, resolution: Tuple[int, int]) -> opencv.VideoCapture:
    camera = Picamera2()
    camera.preview_configuration.main.size = (resolution[0], resolution[1])
    camera.preview_configuration.main.format = "RGB888"
    camera.preview_configuration.align()
    camera.configure("preview")
    camera.start()

    return camera


class RaspiCameraComponent(Camera):
    def __init__(self, channel: int, name: str, resolution: Tuple[int, int], scale: float):
            super().__init__(name=name, channel=channel, resolution=resolution, scale=scale)
            self.camera: Camera = get_camera(channel=channel, logger=self.logger, name=name, resolution=resolution)
            self.framerate: int = self.camera.video_configuration.controls.FrameRate
        
    def read(self):
        super().read()
        image = self.camera.capture_array()
        return image