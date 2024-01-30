def at_unit(time_unit: int, value: int):
    return time_unit == value


def between_units(min_value: int, max_value: int, value: int):
    return min_value <= value and value < max_value


def each_unit(time_unit: int, value: int):
    if value != 0:
        return time_unit % value == 0
    return False


def every_unit():
    return True
