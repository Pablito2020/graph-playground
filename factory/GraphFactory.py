from graphics import *
from graphical.Dimensions import Dimensions
from graphical.PaintGraph import PaintGraph


class GraphFactory:

    def __init__(self, graph):
        self.graph = graph

    def paint(self):
        win = GraphWin("Graph", Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value)
        PaintGraph.paint_graph(win, self.graph)
