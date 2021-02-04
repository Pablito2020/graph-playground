from graph.Graph import Graph
from graph.Node import Node
from graph.Color import ColorPair
from exceptions.NoMoreColorsException import NoMoreColorsException


def greedy_coloring(graph: Graph):
    colors = get_list_colors()
    for i in graph.nodes:
        i.color = paint(i, colors)


def get_list_colors():
    colors = list()
    for color in ColorPair:
        colors.append(color)
    return colors


def paint(node: Node, colors: list):
    colors_adjacent = list()
    for current in node.adjacent_nodes:
        colors_adjacent.append(current.color)
    for color in colors:
        if not_adjacent(color, colors_adjacent):
            return color
    raise NoMoreColorsException()


def not_adjacent(color, colors_adjacent):
    counter = 0
    for current_color in colors_adjacent:
        if color != current_color:
            counter += 1
    return counter == len(colors_adjacent)
