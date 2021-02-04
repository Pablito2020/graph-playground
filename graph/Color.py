from enum import Enum

from graphics import color_rgb
from structure.Pairs import Pairs


# RGB values of the colors
class Color(Enum):
    WHITE = color_rgb(255, 255, 255)
    BLACK = color_rgb(0, 0, 0)
    RED = color_rgb(220, 20, 60)
    GREEN = color_rgb(34, 139, 34)
    BLUE = color_rgb(0, 191, 255)
    ORANGE = color_rgb(255, 69, 0)
    YELLOW = color_rgb(255, 255, 0)


class StockColor(Enum):
    NULL_COLOR = Pairs(Color.BLUE.value, Color.BLACK.value)


class ColorPair(Enum):
    FIRST_COLOR = Pairs(Color.RED.value, Color.WHITE.value)
    SECOND_COLOR = Pairs(Color.ORANGE.value, Color.BLACK.value)
    THIRD_COLOR = Pairs(Color.GREEN.value, Color.WHITE.value)
    FORTH_COLOR = Pairs(Color.YELLOW.value, Color.BLACK.value)
    FIFTH_COLOR = Pairs(Color.BLACK.value, Color.WHITE.value)
    SIXTH_COLOR = Pairs(Color.WHITE.value, Color.BLACK.value)
