from graphical.Dimensions import Dimensions
from graphics import *
from algorithms.DFS import dfs
from graphical.PaintTree import PaintTree


class DFSFactory:

    def __init__(self, graph):
        self.graph = graph

    def paint(self):
        vertex = input("Vertex for DFS: \n")
        while not self.graph.__contains__(vertex):
            vertex = input("Vertex doesn't exists on this graph, please insert other vertex \n")
        dfs_tree = dfs(self.graph, vertex)
        win = GraphWin("DFS result", Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value)
        PaintTree.paint_tree(win, dfs_tree)
