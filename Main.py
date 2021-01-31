from algorithms.BFS import bfs
from files.GraphGetter import GraphGetter
from graphics import *
import random

graph = GraphGetter.get_graph_from_file()
bfs_tree = bfs(graph, "A")

circle_radius = 20
screen_width = 1000
screen_height = 800
safety = 5


def main():
    win = GraphWin("Graphs PlayGround", screen_width, screen_height)
    node_draws = []
    point_history = []
    for current_node in graph.nodes:
        point = None
        while not_valid(point, point_history):
            random_number = random.randint(1, 30)
            x_point = ((screen_width - 2 * circle_radius - safety) * random_number) % (screen_width - 2 * circle_radius)
            y_point = ((screen_height - 2 * circle_radius - safety) * random_number) % (screen_height - 2 * circle_radius)
            point = Point(x_point + circle_radius, y_point + circle_radius)
        point_history.append(point)
        node_draws.append(Circle(point, circle_radius))

    for graphic_node in node_draws:
        graphic_node.setFill(color_rgb(0, 0, 0))
        graphic_node.draw(win)

    win.getMouse()
    win.close()


def not_valid(point: Point, point_history):
    if point is None:
        return True
    for current in point_history:
        if not_valid_point(current, point):
            return True
    return False


def not_valid_point(good: Point, actual: Point):
    return wrong_x(good.getX(), actual.getX()) and wrong_y(good.getY(), actual.getY())


def wrong_x(good_x, test_x):
    return good_x + circle_radius + safety > test_x > good_x - safety - circle_radius


def wrong_y(good_y, test_y):
    return good_y + circle_radius + safety > test_y > good_y - safety - circle_radius


main()
