from algorithms.GreedyColoring import greedy_coloring
from graphics import *
from graphical.Dimensions import Dimensions
from graphical.PaintGraph import PaintGraph


class ColorFactory:

    def __init__(self, graph):
        self.graph = graph

    def paint(self):
        greedy_coloring(self.graph)
        win = GraphWin("Paint Graph", Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value)
        PaintGraph.paint_graph(win, self.graph)
