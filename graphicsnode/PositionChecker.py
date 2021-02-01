from graphics import *

from graphicsnode.Dimensions import Dimensions


class PositionChecker:

    @staticmethod
    def not_valid(point: Point, point_history):
        if point is None:
            return True
        for current in point_history:
            if PositionChecker.not_valid_point(current, point):
                return True
        return False

    @staticmethod
    def not_valid_point(good: Point, actual: Point):
        return PositionChecker.wrong_x(good.getX(), actual.getX()) and PositionChecker.wrong_y(good.getY(),
                                                                                               actual.getY())

    @staticmethod
    def wrong_x(good_x, test_x):
        return good_x + Dimensions.CIRCLE_RADIUS.value + Dimensions.SAFETY_VALUE.value > test_x > good_x - Dimensions.SAFETY_VALUE.value - Dimensions.CIRCLE_RADIUS.value

    @staticmethod
    def wrong_y(good_y, test_y):
        return good_y + Dimensions.CIRCLE_RADIUS.value + Dimensions.SAFETY_VALUE.value > test_y > good_y - Dimensions.SAFETY_VALUE.value - Dimensions.CIRCLE_RADIUS.value
