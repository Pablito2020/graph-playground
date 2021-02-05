from structure.Node import Node
from exceptions.NoElementInGraphException import NoNodeInGraphException


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
        try:
            node = self.get_node(value)
        except NoNodeInGraphException as e:  # code to run if error occurs
            self.nodes.append(Node(value))

    def get_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        raise NoNodeInGraphException()

    def __contains__(self, item):
        for node in self.nodes:
            if node.value == item:
                return True
        return False

    def __str__(self):
        nodes = ""
        for node in self.nodes:
            nodes += str(node) + "\n"
        return nodes
