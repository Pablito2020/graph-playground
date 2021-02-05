from graphical.NodeDraw import NodeDraw
from graphics import *
from structure.Pairs import Pairs
from graphical.Dimensions import Dimensions
from graphical.PositionChecker import PositionChecker
import random

circle_radius = Dimensions.CIRCLE_RADIUS.value
screen_width = Dimensions.SCREEN_WIDTH.value
screen_height = Dimensions.SCREEN_HEIGHT.value
safety = Dimensions.SAFETY_VALUE.value


class PaintGraph:

    @staticmethod
    def paint_graph(win, graph):

        node_draws = []
        point_history = []
        edges = []

        # Save node draw objects in node draws list
        for current_node in graph.nodes:
            point = None
            while PositionChecker.not_valid(point, point_history):
                random_x = random.randint(1, screen_width)
                random_y = random.randint(1, screen_height)
                x_point = (screen_width - 2 * circle_radius - safety + random_x) % (screen_width - 2 * circle_radius)
                y_point = (screen_height - 2 * circle_radius - safety + random_y) % (screen_height - 2 * circle_radius)
                point = Point(x_point + circle_radius, y_point + circle_radius)
            point_history.append(point)
            node_draws.append(NodeDraw((Circle(point, circle_radius)), Text(point, current_node.value), current_node))

        # Add node draw objects to canvas
        for node in node_draws:
            node.circle.setFill(node.value.color.value.first)
            node.circle.draw(win)
            node.text.setTextColor(node.value.color.value.second)
            node.text.draw(win)

        # Get edges
        for current_node in graph.nodes:
            for adjacent in current_node.adjacent_nodes:
                current_pair = Pairs(current_node.value, adjacent.value)
                if not PaintGraph.__edge_exists(edges, current_pair):
                    edges.append(current_pair)

        # Add edges to canvas
        for edge in edges:
            nodes_adjacency = []
            for i in node_draws:
                if edge.first == i.value.value or edge.second == i.value.value:
                    nodes_adjacency.append(i)
            result = PaintGraph.__get_result(nodes_adjacency[0], nodes_adjacency[1])
            line = Line(result[0], result[1])
            line.draw(win)

        win.getMouse()
        win.close()

    @staticmethod
    def __get_result(first_point: NodeDraw, second_point: NodeDraw):
        center_first = first_point.circle.getCenter()
        center_second = second_point.circle.getCenter()

        if center_first.getY() < center_second.getY():
            first_y = center_first.getY() + Dimensions.CIRCLE_RADIUS.value
            final_y = center_second.getY() - Dimensions.CIRCLE_RADIUS.value
        else:
            first_y = center_first.getY() - Dimensions.CIRCLE_RADIUS.value
            final_y = center_second.getY() + Dimensions.CIRCLE_RADIUS.value
        return [Point(center_first.getX(), first_y), Point(center_second.getX(), final_y)]

    @staticmethod
    def __edge_exists(edge_list, pair: Pairs):
        for edge in edge_list:
            if PaintGraph.__equals_edge(edge, pair):
                return True
        return False

    @staticmethod
    def __equals_edge(current_edge: Pairs, edge: Pairs):
        return (current_edge.first == edge.first and current_edge.second == edge.second) or (
                current_edge.second == edge.first and current_edge.first == edge.second)
