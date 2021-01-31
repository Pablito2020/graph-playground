from algorithms.BFS import bfs
from files.GraphGetter import GraphGetter
from graphics import *

# def main():
# win = GraphWin("Graphs PlayGround", 500, 500)
# point = Point(250, 250)
# cir = Circle(point, 50)
# cir.draw(win)
# win.getMouse()
# win.close()
#
# main()

graph = GraphGetter.get_graph_from_file()
bfs_tree = bfs(graph, "A")
print("This is only for testing")