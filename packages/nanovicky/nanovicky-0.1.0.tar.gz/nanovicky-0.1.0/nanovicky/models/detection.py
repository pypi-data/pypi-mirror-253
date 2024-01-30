from datetime import datetime

from models import Data
from utils import BBox


class Detection:
    def __init__(
        self, bbox: BBox, time: datetime = datetime.now(), obj: Data = None
    ) -> None:
        self._object: Data = obj
        self._bbox: BBox = bbox
        self._timestamp: datetime = time
