from graphics import *

from algorithms.BFS import bfs
from algorithms.DFS import dfs
from graphicsnode.PaintGraph import PaintGraph
from graph.Graph import Graph
from graphicsnode.Dimensions import Dimensions
from graphicsnode.PaintTree import PaintTree
from algorithms.GreedyColoring import greedy_coloring


class ChoosePaint:

    @staticmethod
    def chooser(graph: Graph):
        option = ""
        while not ChoosePaint.correct_option(option):
            option = input("Input: \n g|G) Print the graph \n b|B) Make BFS \n d|D Make DFS \n c|C Color the graph \n")

        option = option.lower()
        if option == "g":
            win = GraphWin("Graph", Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value)
            PaintGraph.paint_graph(win, graph)

        if option == "b":
            vertex = input("Vertex for BFS: \n")
            while not graph.__contains__(vertex):
                vertex = input("Vertex doesn't exists on this graph, please insert other vertex \n")
            tree = bfs(graph, vertex)
            win = GraphWin("BFS result", Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value)
            PaintTree.paint_tree(win, tree)

        if option == "d":
            vertex = input("Vertex for DFS: \n")
            while not graph.__contains__(vertex):
                vertex = input("Vertex doesn't exists on this graph, please insert other vertex \n")
            tree = dfs(graph, vertex)
            win = GraphWin("DFS result", Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value)
            PaintTree.paint_tree(win, tree)

        if option == "c":
            greedy_coloring(graph)
            win = GraphWin("Paint Graph", Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value)
            PaintGraph.paint_graph(win, graph)

    @staticmethod
    def correct_option(str):
        str = str.lower()
        return str == "g" or str == "b" or str == "d" or str == "c"
