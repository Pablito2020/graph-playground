from structure.Graph import Graph
from structure.Node import Node
from colors.Color import ColorPair
from exceptions.NoMoreColorsException import NoMoreColorsException


def greedy_coloring(graph: Graph):
    colors = __get_list_colors()
    for i in graph.nodes:
        i.color = __paint(i, colors)


def __get_list_colors():
    colors = list()
    for color in ColorPair:
        colors.append(color)
    return colors


def __paint(node: Node, colors: list):
    colors_adjacent = list()
    for current in node.adjacent_nodes:
        colors_adjacent.append(current.color)
    for color in colors:
        if __not_adjacent(color, colors_adjacent):
            return color
    raise NoMoreColorsException()


def __not_adjacent(color, colors_adjacent):
    counter = 0
    for current_color in colors_adjacent:
        if color != current_color:
            counter += 1
    return counter == len(colors_adjacent)
