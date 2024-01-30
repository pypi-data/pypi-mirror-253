from utils import Point

from math import sqrt


def middle_point(pt1: Point, pt2: Point) -> Point:
    """Returns the middle point, between two points.

    Args:
        pt1 (Point): First point
        pt2 (Point): Second point

    Returns:
        Point: The middle point.
    """
    return Point(
        int((pt2.x + pt1.x) / 2),
        int((pt2.y + pt1.y) / 2),
    )


def points_distance(pt1: Point, pt2: Point) -> int:
    """Returns the distance between two point.

    Args:
        pt1 (Point): The first point
        pt2 (Point): The second point

    Returns:
        int: The distance between the two points
    """
    return int(((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2) ** 0.5)
