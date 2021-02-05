from structure.Graph import Graph
from structure.Tree import Tree
from structure.Pairs import Pairs


def bfs(graph: Graph, value):
    array = __bfs_helper(graph, value)
    tree = Tree(array.pop(0).first.value)
    for i in array:
        actual = tree.get_tree(i.second.value)
        actual.add_descendant(Tree(i.first.value))
    return tree


def __bfs_helper(graph: Graph, value):
    visited = []
    queue = [Pairs(graph.get_node(value), None)]
    while queue:
        pair = queue.pop(0)
        node = pair.first
        parent = pair.second
        if not __in_visited(visited, node):
            visited.append(Pairs(node, parent))
        for neighbour in node.adjacent_nodes:
            if not __in_visited(visited, neighbour):
                queue.append(Pairs(neighbour, node))
    return visited


def __in_visited(visited, node):
    for i in visited:
        if i.first.value == node.value:
            return True
    return False

