from __future__ import annotations  # Pour permettre le typage des annotations vers des classes définies plus tard
import cv2 as opencv
import numpy as np


from helper.geometry import middle_point
from shapes import Point
from drawing import Drawables, Color

class BBox(Drawables):
    def __init__(self, pt1: Point, pt2: Point, color: Color = None, conf: float = 0.0, label: str = "") -> None:
        super().__init__(color)
        self._pt1 = pt1
        self._pt2 = pt2
        self.conf = conf
        self.label = label

    def draw(self, image, color: Color = None):
        used_color: Color = self._color if color is None else color
        opencv.rectangle(
            image, self._pt1.value(), self._pt2.value(), used_color.cv_color(), 1
        )

    def center(self) -> Point:
        return middle_point(self._pt1, self._pt2)

    def top(self) -> Point:
        return middle_point(self._pt1, Point(self.pt2.x, self.pt1.y))

    def bottom(self) -> Point:
        return middle_point(Point(self.pt1.x, self.pt2.y), self._pt2)

    def bounding_box(self):
        return self
    

    def calculate_distance(self: BBox, other_bbox: BBox) -> float:
        center1 = self.center().value()
        center2 = other_bbox.center().value()

        distance = np.linalg.norm(np.array(center1) - np.array(center2))
        return distance

    def is_close(self, other_bbox: BBox, max_distance: float) -> bool:
        distance: float = self.calculate_distance(other_bbox)
        return distance < max_distance

    def is_inside(self, other_box: BBox) -> bool:
        x1_min, y1_min = min(self._pt1.x, self._pt2.x), min(self._pt1.y, self._pt2.y)
        x1_max, y1_max = max(self._pt1.x, self._pt2.x), max(self._pt1.y, self._pt2.y)

        x2_min, y2_min = min(other_box._pt1.x, other_box._pt2.x), min(other_box._pt1.y, other_box._pt2.y)
        x2_max, y2_max = max(other_box._pt1.x, other_box._pt2.x), max(other_box._pt1.y, other_box._pt2.y)
        
        return x2_min <= x1_min and y2_min <= y1_min and x2_max >= x1_max and y2_max >= y1_max
    
    def calculate_area(self) -> float:
        width = max(0, self._pt2.x - self._pt1.x)
        height = max(0, self._pt2.y - self._pt1.y)
        return width * height
    
    def calculate_intersection_area(self, other_box: BBox) -> float:
        x_overlap = max(0, min(self._pt2.x, other_box._pt2.x) - max(self._pt1.x, other_box._pt1.x))
        y_overlap = max(0, min(self._pt2.y, other_box._pt2.y) - max(self._pt1.y, other_box._pt1.y))
        return x_overlap * y_overlap

    def calculate_union_area(self, other_box: BBox) -> float:
        area_self = self.calculate_area()
        area_other = other_box.calculate_area()
        intersection_area = self.calculate_intersection_area(other_box)
        union_area = area_self + area_other - intersection_area
        return union_area

    def calculate_iou(self, other_box: BBox) -> float:
        intersection_area = self.calculate_intersection_area(other_box)
        union_area = self.calculate_union_area(other_box)
        if union_area == 0:
            return 0.0
        iou = intersection_area / union_area
        return iou

    # using Jaccard indice (min_iou) to control overlap pourcentage
    def is_overlapping(self, other_box: BBox, min_iou: float) -> bool:
        iou = self.calculate_iou(other_box)
        return iou > min_iou
    
    def get_global_box(self, other_box: BBox) -> BBox:
        x_min_global: int = min(self._pt1.x, other_box._pt1.x)
        y_min_global: int = min(self._pt1.y, other_box._pt1.y)
        x_max_global: int = max(self._pt2.x, other_box._pt2.x)
        y_max_global: int = max(self._pt2.y, other_box._pt2.y)

        global_box: BBox = BBox(Point(x_min_global, y_min_global), Point(x_max_global, y_max_global))

        return global_box

    @property
    def pt1(self):
        return self._pt1

    @property
    def pt2(self):
        return self._pt2

    @property
    def width(self):
        return self._pt2.x - self._pt1.x

    @property
    def height(self):
        return self._pt2.y - self._pt1.y

    def __str__(self) -> str:
        return f"({self._pt1.x}, {self._pt1.y}) ({self._pt2.x}, {self._pt2.y})"
