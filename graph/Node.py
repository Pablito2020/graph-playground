class Node:

    def __init__(self, value):
        self.value = value
        self.adjacent_nodes = []

    def adjacent(self, node):
        if not self.is_adjacent(node):
            self.adjacent_nodes.append(node)
            node.adjacent_nodes.append(self)

    def is_adjacent(self, node_2):
        for x in self.adjacent_nodes:
            if x.value == node_2.value:
                return True
        return False
