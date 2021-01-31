from exceptions.NoElementInGraphException import no_node_in_graph_exception
from graph.Graph import Graph
from tree.Tree import Tree


def bfs(graph: Graph, num):
    tree = bfs_recursive(graph, num, [])
    return tree


def bfs_recursive(graph: Graph, num, visited_nodes):
    current_node = graph.get_node(num)
    if current_node is None:
        raise no_node_in_graph_exception()
    visited_nodes.append(num)
    tree = Tree(num)
    current = []
    for adjacent_node in current_node.adjacent_nodes:
        if adjacent_node.value not in visited_nodes:
            current.append(adjacent_node.value)
    for node in current:
        tree.add_descendant(bfs_recursive(graph, node, visited_nodes))
    return tree
