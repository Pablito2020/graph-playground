from algorithms.BFS import bfs
from files.GraphGetter import GraphGetter
from graphics import *
from graphicsnode.Dimensions import Dimensions
from graphicsnode.PaintGraph import PaintGraph

win = GraphWin("Graphs PlayGround", Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value)

# Graph and BFS of all vertices
graph = GraphGetter.get_graph_from_file()
bfs_trees = []
for i in graph.nodes:
    bfs_trees.append(bfs(graph, i.value))
graph_painter = PaintGraph.paint_graph(win, graph)
