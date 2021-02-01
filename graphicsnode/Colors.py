from enum import Enum

from graphics import color_rgb


class Color(Enum):
    WHITE = color_rgb(255, 255, 255)
    BLACK = color_rgb(0, 0, 0)
    RED = color_rgb(220, 20, 60)
    GREEN = color_rgb(34, 139, 34)
    BLUE = color_rgb(0, 191, 255)
    ORANGE = color_rgb(255, 69, 0)
    YELLOW = color_rgb(255, 255, 0)
