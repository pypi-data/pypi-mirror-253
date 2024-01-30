from random import randint

from helper import hexadecimal_to_rgb


class Color:
    def __init__(self, red: int, green: int, blue: int) -> None:
        self._red = red
        self._green = green
        self._blue = blue

    def color(self):
        return self._red, self._green, self._blue

    def cv_color(self):
        return self._blue, self._green, self._red

    @property
    def red(self):
        return self._red

    @property
    def green(self):
        return self._green

    @property
    def blue(self):
        return self._blue


class RandomColor(Color):
    def __init__(self) -> None:
        super().__init__(randint(0, 255), randint(0, 255), randint(0, 255))


class HexadecimalColor(Color):
    def __init__(self, hexcode: str) -> None:
        super().__init__(*hexadecimal_to_rgb(hexcode))
