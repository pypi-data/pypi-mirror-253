from typing import Dict, List, Tuple

from helper import middle_point, points_distance
from utils import Colors, Drawables, Segment, Point, BBox

class Pose(Drawables):
    def __init__(
        self,
        nose,
        left_eye: Point,
        right_eye: Point,
        left_ear: Point,
        right_ear: Point,
        left_shoulder: Point,
        right_shoulder: Point,
        left_elbow: Point,
        right_elbow: Point,
        left_wrist: Point,
        right_wrist: Point,
        left_hip: Point,
        right_hip: Point,
        left_knee: Point,
        right_knee: Point,
        left_ankle: Point,
        right_ankle: Point,
    ) -> None:
        self._nose: Point = nose
        self._left_eye: Point = left_eye
        self._right_eye: Point = right_eye
        self._left_ear: Point = left_ear
        self._right_ear: Point = right_ear
        self._left_shoulder: Point = left_shoulder
        self._right_shoulder: Point = right_shoulder
        self._left_elbow: Point = left_elbow
        self._right_elbow: Point = right_elbow
        self._left_wrist: Point = left_wrist
        self._right_wrist: Point = right_wrist
        self._left_hip: Point = left_hip
        self._right_hip: Point = right_hip
        self._left_knee: Point = left_knee
        self._right_knee: Point = right_knee
        self._left_ankle: Point = left_ankle
        self._right_ankle: Point = right_ankle

    def keypoints(self) -> List[Point]:
        return [
            self._nose,
            self._left_eye,
            self._right_eye,
            self._left_ear,
            self._right_ear,
            self._left_shoulder,
            self._right_shoulder,
            self._left_elbow,
            self._right_elbow,
            self._left_wrist,
            self._right_wrist,
            self._left_hip,
            self._right_hip,
            self._left_knee,
            self._right_knee,
            self._left_ankle,
            self._right_ankle,
        ]

    def ground_position(self) -> Point:
        return (
            middle_point(self._left_ankle, self._right_ankle).set_color(Colors.BLUE)
            if all(
                coordinate > 0
                for coordinate in [
                    *self._left_ankle.value(),
                    *self._right_ankle.value(),
                ]
            )
            else None
        )

    def body_orientation(self) -> Tuple[Point]:
        return (
            self._left_shoulder,
            self._right_shoulder
            if all(
                coordinate > 0
                for coordinate in [
                    *self._left_shoulder.value(),
                    *self._right_shoulder.value(),
                ]
            )
            else None,
        )

    def main_axis_coeff(self) -> int:
        """Returns the main axis distance, which is used to reduce all bones distance.

        Returns:
            int: The main axis coeef.
        """
        pt1: Point = middle_point(self._left_shoulder, self._right_shoulder)
        pt2: Point = middle_point(self._left_hip, self._right_hip)

        return points_distance(pt1, pt2)

    def bounding_box(self) -> BBox:
        keypoints = self.keypoints()
        x1 = min([point.x for point in keypoints if point.x > 0])
        x2 = max([point.x for point in keypoints if point.x > 0])
        y1 = min([point.y for point in keypoints if point.y > 0])
        y2 = max([point.y for point in keypoints if point.y > 0])
        return BBox(Point(x1, y1), Point(x2, y2))

    def __str__(self) -> str:
        return f"""
nose : {self._nose.value()}
left_eye : {self._left_eye.value()}
right_eye : {self._right_eye.value()}
left_ear : {self._left_ear.value()}
right_ear : {self._right_ear.value()}
left_shoulder : {self._left_shoulder.value()}
right_shoulder : {self._right_shoulder.value()}
left_elbow : {self._left_elbow.value()}
right_elbow : {self._right_elbow.value()}
left_wrist : {self._left_wrist.value()}
right_wrist : {self._right_wrist.value()}
left_hip : {self._left_hip.value()}
right_hip : {self._right_hip.value()}
left_knee : {self._left_knee.value()}
right_knee : {self._right_knee.value()}
left_ankle : {self._left_ankle.value()}
right_ankle : {self._right_ankle.value()}
        """

    def axis(self) -> Dict[str, Segment]:
        """Return the pose as named axis.

        Returns:
            Dict[str, Segment]: The pose axis with name : line.
        """
        return {
            # Facial feature
            "face_left": Segment(self._left_ear, self._left_eye, Colors.hex("#15edd8")),
            "face_right": Segment(
                self._right_ear, self._right_eye, Colors.hex("#15edd8")
            ),
            "face_left_center": Segment(
                self._left_eye, self._nose, Colors.hex("#3705ff")
            ),
            "face_right_center": Segment(
                self._right_eye, self._nose, Colors.hex("#3705ff")
            ),
            # Arms
            "left_arm": Segment(
                self._left_shoulder, self._left_elbow, Colors.hex("#ff4287")
            ),
            "left_forharm": Segment(
                self._left_elbow, self._left_wrist, Colors.hex("#b38df0")
            ),
            "right_arm": Segment(
                self._right_shoulder, self._right_elbow, Colors.hex("#ff4287")
            ),
            "right_forharm": Segment(
                self._right_elbow, self._right_wrist, Colors.hex("#b38df0")
            ),
            # Trunc
            "upper_trunc": Segment(
                self._left_shoulder, self._right_shoulder, Colors.hex("#e83f10")
            ),
            "right_trunc": Segment(
                self._right_shoulder, self._right_hip, Colors.hex("#ff7f5c")
            ),
            "left_trunc": Segment(
                self._left_shoulder, self._left_hip, Colors.hex("#ff7f5c")
            ),
            "lower_trunc": Segment(
                self._left_hip, self._right_hip, Colors.hex("#fab700")
            ),
            # Lengs
            "left_leg": Segment(self._left_hip, self._left_knee, Colors.hex("#b4ed15")),
            "left_tibia": Segment(
                self._left_knee, self._left_ankle, Colors.hex("#b4ed15")
            ),
            "right_leg": Segment(
                self._right_hip, self._right_knee, Colors.hex("#c1f59f")
            ),
            "right_tibia": Segment(
                self._right_knee, self._right_ankle, Colors.hex("#c1f59f")
            ),
        }

    def draw(self, image):
        # self.bounding_box().draw(image)
        [
            part.draw(image)
            for part in self.axis().values()
            if all(
                coordinate > 0 for coordinate in [*part.pt1.value(), *part.pt2.value()]
            )
        ]
