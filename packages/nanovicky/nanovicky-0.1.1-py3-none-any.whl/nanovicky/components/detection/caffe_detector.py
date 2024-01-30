import cv2 as opencv

from models import Frame
from components import BaseDetectorComponent


class CaffeDetectorComponent(BaseDetectorComponent):
    def __init__(self, name: str, proto_file: str, model_file: str):
        super().__init__(name=name)
        self._detector = opencv.dnn.readNetFromCaffe(proto_file, model_file)

    def do(self):
        frame: Frame = self._inputs["frames"].get()

        if frame is not None:
            blob = opencv.dnn.blobFromImage(
                frame.image,
                scalefactor=0.007843,
                size=(300, 300),
                mean=(127.5, 127.5, 127.5),
                swapRB=True,
            )

            self._detector.setInput(blob)

            self._detector.forward()

            if self._outputs["frames"].is_linked():
                self._outputs["frames"].set(frame)

            if self._outputs["detections"].is_linked():
                self._outputs["detections"].set([])
