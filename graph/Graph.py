from graph.Node import Node


class Graph:

    def __init__(self):
        self.nodes = []

    def add_node(self, value, list_adjacency):
        self.add_if_not_exists(value)
        node = self.get_node(value)
        for i in list_adjacency:
            self.add_if_not_exists(i)
            node2 = self.get_node(i)
            node.adjacent(node2)

    def add_if_not_exists(self, value):
        node = self.get_node(value)
        if node is None:
            self.nodes.append(Node(value))

    def get_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def __str__(self):
        nodes = ""
        for node in self.nodes:
            nodes += str(node) + "\n"
        return nodes
