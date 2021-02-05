from algorithms.BFS import bfs
from graphics import *
from graphical.Dimensions import Dimensions
from graphical.PaintTree import PaintTree


class BFSFactory:

    def __init__(self, graph):
        self.graph = graph

    def paint(self):
        vertex = input("Vertex for BFS: \n")
        while not self.graph.__contains__(vertex):
            vertex = input("Vertex doesn't exists on this graph, please insert other vertex \n")
        tree = bfs(self.graph, vertex)
        win = GraphWin("BFS result", Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value)
        PaintTree.paint_tree(win, tree)
