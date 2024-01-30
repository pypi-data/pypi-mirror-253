from typing import Tuple, List

import cv2 as opencv
from drawing import Color, Drawables, Colors
from dataclasses import dataclass


def point(x: int, y: int):
    return int(x), int(y)


@dataclass
class Point:
    x: int
    y: int
    color: Color = Colors.RED
    # def __init__(self, x: int, y: int, color: Color = None) -> None:
    #     super().__init__(color)
    #     self._x = x
    #     self._y = y

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def value(self) -> Tuple[int, int]:
        return self.x, self.y

    def draw(self, image, color: Color = None):
        opencv.circle(image, self.value(), 1, color.cv_color(), -1)


class Segment(Drawables):
    def __init__(self, pt1: Point, pt2: Point, color: Color = None) -> None:
        super().__init__(color)
        self._pt1 = pt1
        self._pt2 = pt2

    def value(self) -> Tuple[Point, Point]:
        return self._pt1, self._pt2

    def draw(self, image, color: Color = None):
        col: Color = super().draw(image)
        opencv.line(image, self._pt1.value(), self._pt2.value(), col.cv_color(), 1)

    @property
    def pt1(self):
        return self._pt1

    @property
    def pt2(self):
        return self._pt2


class Line(Drawables):
    def __init__(self, points: List[Point], color: Color = None) -> None:
        super().__init__(color)
        self._points = points

    @property
    def points(self):
        return self._points

    def draw(self, image, color: Color = None) -> Color:
        col: Color = super().draw(image)
        for pt1, pt2 in zip(self._points, self._points[1:]):
            opencv.line(image, pt1.value(), pt2.value(), col.cv_color(), 2)
