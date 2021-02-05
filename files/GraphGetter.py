from structure.Graph import Graph
from files.File import File

name_file = "graph.txt"


class GraphGetter:

    @staticmethod
    def get_graph_from_file():
        graph = Graph()
        file = File(name_file)
        while file.has_more_edges_to_add():
            current = file.get_edge()
            graph.add_node(current.first, current.second)
        return graph
