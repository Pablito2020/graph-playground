from files.GraphGetter import GraphGetter
from factory.Factory import Factory

# Get graph from file
graph = GraphGetter.get_graph_from_file()

# Get option
option = ""
while not Factory.correct_option(option):
    option = input("Input: \n g|G) Print the graph \n b|B) Make BFS \n d|D) Make DFS \n c|C) Color the graph \n")

# Paint Graph
element = Factory.get_painting(option, graph)
element.paint()
