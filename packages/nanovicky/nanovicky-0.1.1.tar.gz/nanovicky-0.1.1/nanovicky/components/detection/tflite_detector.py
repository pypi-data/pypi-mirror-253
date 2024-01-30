from typing import List
import re

import cv2 as opencv

# import tensorflow.lite as tflite
import tflite_runtime.interpreter as tflite
import numpy as np
from PIL import Image

from components import BaseDetectorComponent
from models import Frame
from utils import BBox
from utils import Point


class TFLiteDetectorComponent(BaseDetectorComponent):
    def __init__(self, name: str, detector_path: str, labels_path: str):
        super().__init__(name=name)
        self._detector_path: str = detector_path
        self._label_path: str = labels_path
        self._labels = self.load_labels()
        self._interpreter: tflite.Interpreter = self.load_model()
        self._input_details = self._interpreter.get_input_details()

        self._input_shape = self._input_details[0]["shape"]
        self._height = self._input_shape[1]
        self._width = self._input_shape[2]

        self._input_index = self._input_details[0]["index"]

    def load_labels(self):
        with open(self._label_path) as f:
            labels = {}
            for line in f.readlines():
                m = re.match(r"(\d+)\s+(\w+)", line.strip())
                labels[int(m.group(1))] = m.group(2)
            return labels

    def load_model(self):
        interpreter = tflite.Interpreter(
            model_path=self._detector_path,
            experimental_delegates=[tflite.load_delegate("libedgetpu.so.1")],
        )
        interpreter.allocate_tensors()
        return interpreter

    def do(self):
        frame: Frame = self.inputs["frames"].get()

        if frame is not None:
            rescaled_image = opencv.resize(
                frame.image,
                (self._width, self._height),
                interpolation=opencv.INTER_AREA,
            )
            image = Image.fromarray(
                opencv.cvtColor(rescaled_image, opencv.COLOR_BGR2RGB)
            )

            # Aplly detection
            input_data = np.expand_dims(image, axis=0)
            self._interpreter.set_tensor(self._input_index, input_data)
            self._interpreter.invoke()

            # Get outputs
            output_details = self._interpreter.get_output_details()
            # output_details[0] - position
            # output_details[1] - class id
            # output_details[2] - score
            # output_details[3] - count

            positions = np.squeeze(
                self._interpreter.get_tensor(output_details[0]["index"])
            )
            np.squeeze(self._interpreter.get_tensor(output_details[1]["index"]))
            scores = np.squeeze(
                self._interpreter.get_tensor(output_details[2]["index"])
            )

            result = []

            np.array(image)

            for idx, score in enumerate(scores):
                if score > 0.5:
                    x1 = int(positions[idx][1] * frame.image.shape[1])
                    x2 = int(positions[idx][3] * frame.image.shape[1])
                    y1 = int(positions[idx][0] * frame.image.shape[0])
                    y2 = int(positions[idx][2] * frame.image.shape[0])
                    result.append(BBox(Point(x1, y1), Point(x2, y2)))
                    # opencv.rectangle(new_image, (x1, y1), (x2, y2), (0, 255, 0), 1)

            if self._outputs["frames"].is_linked():
                self._outputs["frames"].set(frame)

            if self._outputs["detections"].is_linked():
                self._outputs["detections"].set(result)
