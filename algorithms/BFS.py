from graph.Graph import Graph
from tree.Tree import Tree


def bfs(graph: Graph, value):
    tree = bfs_recursive(graph, value, [])
    return tree


def bfs_recursive(graph: Graph, value, visited_nodes):
    current_node = graph.get_node(value)
    visited_nodes.append(value)
    tree = Tree(value)
    current = []
    for adjacent_node in current_node.adjacent_nodes:
        if adjacent_node.value not in visited_nodes:
            current.append(adjacent_node.value)
    for node in current:
        tree.add_descendant(bfs_recursive(graph, node, visited_nodes))
    return tree
