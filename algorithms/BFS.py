from graph.Graph import Graph
from tree.Tree import Tree
from structure.Pairs import Pairs


def bfs(graph: Graph, value):
    array = bfs_helper(graph, value)
    tree = Tree(array.pop(0).first.value)
    for i in array:
        actual = tree.get_tree(i.second.value)
        actual.add_descendant(Tree(i.first.value))
    return tree


def bfs_helper(graph: Graph, value):
    visited = []
    queue = [Pairs(graph.get_node(value), None)]
    while queue:
        pair = queue.pop(0)
        node = pair.first
        parent = pair.second
        if not in_visited(visited, node):
            visited.append(Pairs(node, parent))
        for neighbour in node.adjacent_nodes:
            if not in_visited(visited, neighbour):
                queue.append(Pairs(neighbour, node))
    return visited


def in_visited(visited, node):
    for i in visited:
        if i.first.value == node.value:
            return True
    return False

