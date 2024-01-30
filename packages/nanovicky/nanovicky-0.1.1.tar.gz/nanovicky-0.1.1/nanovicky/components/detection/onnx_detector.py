import cv2 as opencv

from components import BaseDetectorComponent
from models import Frame


class ONNXDetectorComponent(BaseDetectorComponent):
    def __init__(self, name: str, model_path: str):
        super().__init__(name=name)
        self._model_path: str = model_path
        self._net = opencv.dnn.readNetFromONNX(self._model_path)

    def do(self):
        frame: Frame = self._inputs["frames"].get()

        if frame is not None:
            blob = opencv.dnn.blobFromImage(
                frame.image, 1 / 255, (640, 640), [0, 0, 0], 1, crop=False
            )

            # Sets the input to the network.
            self._net.setInput(blob)

            # Runs the forward pass to get output of the output layers.
            output_layers = self._net.getUnconnectedOutLayersNames()
            outputs = self._net.forward(output_layers)

            print(outputs)
