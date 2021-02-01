from graphics import *

from algorithms.BFS import bfs
from graphicsnode.PaintGraph import PaintGraph
from graph.Graph import Graph
from graphicsnode.Dimensions import Dimensions
from graphicsnode.PaintTree import PaintTree


class ChoosePaint:

    @staticmethod
    def chooser(graph: Graph):
        option = ""
        while not ChoosePaint.correct_option(option):
            option = input("Input: \n g|G) Print the graph \n b|B) Make BFS ")

        option = option.lower()
        if option == "g":
            win = GraphWin("Graphs PlayGround", Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value)
            PaintGraph.paint_graph(win, graph)
        if option == "b":
            vertex = input("Vertex for BFS: ")
            while not graph.__contains__(vertex):
                vertex = input("Vertex doesn't exists on this graph, please insert other vertex")
            tree = bfs(graph, vertex)
            win = GraphWin("Graphs PlayGround", Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value)
            PaintTree.paint_tree(win, tree)

    @staticmethod
    def correct_option(str):
        str = str.lower()
        return str == "g" or str == "b"
