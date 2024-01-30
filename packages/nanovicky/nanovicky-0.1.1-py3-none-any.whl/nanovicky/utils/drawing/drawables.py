from drawing import Color, Colors

DEFAULT_COLOR: Color = Colors.RED


class Drawables:
    def __init__(self, color: Color = DEFAULT_COLOR) -> None:
        self._color = color if color is not None else DEFAULT_COLOR

    def draw(self, image, color: Color = None) -> Color:
        return self._color if color is None else color

    def set_color(self, color: Color):
        self._color = color
        return self
