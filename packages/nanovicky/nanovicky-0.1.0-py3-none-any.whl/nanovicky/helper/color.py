from typing import Tuple


def hexadecimal_to_rgb(hexcode: str) -> Tuple[int, int, int]:
    """Return the rgb values as a tuple, from a hexadecimal code.

    Args:
        hexcode (str): The hexadecimal code.

    Returns:
        Tuple[int, int, int]: The Red, Green, Blue values.
    """
    return tuple(int(hexcode.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))
