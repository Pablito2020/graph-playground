from graph.Color import StockColor


class Node:

    def __init__(self, value):
        self.value = value
        self.adjacent_nodes = []
        self.color = StockColor.NULL_COLOR

    def adjacent(self, node):
        if not self.is_adjacent(node):
            self.adjacent_nodes.append(node)
            node.adjacent_nodes.append(self)

    def is_adjacent(self, node_2):
        for x in self.adjacent_nodes:
            if x.value == node_2.value:
                return True
        return False

    def change_node_color(self, new_color):
        self.color = new_color

    def __str__(self):
        adjacent_nodes_str = ""
        for current in self.adjacent_nodes:
            adjacent_nodes_str += f"{current.value},"
        return f"Value Node: {self.value}, Adjacent nodes: {adjacent_nodes_str}"
