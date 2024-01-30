from typing import List

import cv2 as opencv
from pycoral.adapters.common import input_size
from pycoral.adapters.detect import get_objects
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter
from pycoral.utils.edgetpu import run_inference

from components.detection.base_detector import BaseDetectorComponent
from models.frame import Frame
from utils.shapes.bbox import BBox
from utils.shapes.shapes import Point


def append_objs_to_img(cv2_im, inference_size, objs, labels):
    height, width, channels = cv2_im.shape
    scale_x, scale_y = width / inference_size[0], height / inference_size[1]
    for obj in objs:
        bbox = obj.bbox.scale(scale_x, scale_y)
        x0, y0 = int(bbox.xmin), int(bbox.ymin)
        x1, y1 = int(bbox.xmax), int(bbox.ymax)

        percent = int(100 * obj.score)
        label = "{}% {}".format(percent, labels.get(obj.id, obj.id))

        cv2_im = opencv.rectangle(cv2_im, (x0, y0), (x1, y1), (0, 255, 0), 2)
        cv2_im = opencv.putText(
            cv2_im,
            label,
            (x0, y0 + 30),
            opencv.FONT_HERSHEY_SIMPLEX,
            1.0,
            (255, 0, 0),
            2,
        )
    return cv2_im


class CoralDevDetectorComponent(BaseDetectorComponent):
    def __init__(
        self,
        model_path: str,
        labels_path: str,
        threshold: float = 0.1,
        name: str = "CoralDevDetectorComponent",
    ):
        super().__init__(name=name)
        self._model_path: str = model_path
        self._labels_path: str = labels_path
        self._interpreter = make_interpreter(self._model_path)
        self._interpreter.allocate_tensors()
        self._labels = read_label_file(self._labels_path)
        self._inference_size = input_size(self._interpreter)
        self._threshold: float = threshold
        self._top_category: int = 3

    def do(self):
        frame: Frame = self._inputs["frames"].get()
        detections: List[BBox] = []

        if frame is not None:
            opencv_im_rgb = opencv.cvtColor(frame.image, opencv.COLOR_BGR2RGB)
            opencv_im_rgb = opencv.resize(opencv_im_rgb, self._inference_size)
            run_inference(self._interpreter, opencv_im_rgb.tobytes())
            objs = [
                obj
                for obj in get_objects(self._interpreter, self._threshold)[
                    : self._top_category
                ]
                if obj.id == 0
            ]  # and obj.score * 100 >= 50]

            # # Old way
            # new_frame = append_objs_to_img(
            #     frame.image, self._inference_size, objs, self._labels
            # )

            # Extract objs into Bboxes
            height, width, channels = frame.image.shape
            scale_x, scale_y = (
                width / self._inference_size[0],
                height / self._inference_size[1],
            )
            for obj in objs:
                bbox = obj.bbox.scale(scale_x, scale_y)
                detections.append(
                    BBox(
                        Point(int(bbox.xmin), int(bbox.ymin)),
                        Point(int(bbox.xmax), int(bbox.ymax)),
                    )
                )

            if self._outputs["frames"].is_linked():
                # Draw detections on image
                # [detection.draw(frame.image) for detection in detections]
                self._outputs["frames"].set(frame)

            if self.outputs["detections"].is_linked():
                self._outputs["detections"].set(detections)
