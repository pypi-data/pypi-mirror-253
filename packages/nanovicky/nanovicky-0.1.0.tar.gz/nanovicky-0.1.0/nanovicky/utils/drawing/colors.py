from drawing import Color, HexadecimalColor, RandomColor


class Colors:
    RED: Color = Color(255, 0, 0)
    GREEN: Color = Color(0, 255, 0)
    BLUE: Color = Color(0, 0, 255)
    WHITE: Color = Color(255, 255, 255)
    BLACK: Color = Color(0, 0, 0)
    RANDOM: Color = RandomColor()

    def hex(hexcode: str):
        return HexadecimalColor(hexcode)

    def random():
        return RandomColor()
