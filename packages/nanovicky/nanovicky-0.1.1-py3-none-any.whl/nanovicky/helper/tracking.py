from utils import BBox


def get_iou(bbox1: BBox, bbox2: BBox) -> float:
    """Return the intersection over union between two bounding boxes.

    Args:
        bbox1 (BBox): The first bounding box.
        bbox2 (BBox): The second bounding box.

    Returns:
        float: The iou coeff.
    """

    bb1 = {
        "x1": bbox1.pt1.value()[0],
        "x2": bbox1.pt2.value()[0],
        "y1": bbox1.pt1.value()[1],
        "y2": bbox1.pt2.value()[1],
    }
    bb2 = {
        "x1": bbox2.pt1.value()[0],
        "x2": bbox2.pt2.value()[0],
        "y1": bbox2.pt1.value()[1],
        "y2": bbox2.pt2.value()[1],
    }

    # determine the coordinates of the intersection rectangle
    x_left = max(bb1["x1"], bb2["x1"])
    y_top = max(bb1["y1"], bb2["y1"])
    x_right = min(bb1["x2"], bb2["x2"])
    y_bottom = min(bb1["y2"], bb2["y2"])

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    # The intersection of two axis-aligned bounding boxes is always an
    # axis-aligned bounding box
    intersection_area = (x_right - x_left) * (y_bottom - y_top)

    # compute the area of both AABBs
    bb1_area = (bb1["x2"] - bb1["x1"]) * (bb1["y2"] - bb1["y1"])
    bb2_area = (bb2["x2"] - bb2["x1"]) * (bb2["y2"] - bb2["y1"])

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
    return iou
