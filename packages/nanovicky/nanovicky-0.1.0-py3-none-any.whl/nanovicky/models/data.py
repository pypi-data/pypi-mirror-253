from typing import Dict

from utils import Drawables


class Data(Drawables):
    def __init__(self, index: int, elements: Dict = {}) -> None:
        self._index: int = index
        self._elements: Dict[str, Dict] = elements

    def draw(self):
        ...
