from structure.Graph import Graph
from structure.Tree import Tree
from collections import deque
from structure.Pairs import Pairs


def dfs(graph: Graph, value):
    node = graph.get_node(value)
    visited = []
    stack = deque()
    visited.append(node.value)
    tree = Tree(value)
    stack.append(Pairs(node, tree))
    while stack:
        current_element = stack.pop()
        if __has_valid_descendant(current_element.first, visited):
            element = __get_valid_descendant(current_element.first, visited)
            new_tree = Tree(element.value)
            current_element.second.add_descendant(new_tree)
            visited.append(element.value)
            stack.append(current_element)
            stack.append(Pairs(element, new_tree))

    return tree


def __has_valid_descendant(node, visited):
    return __get_valid_descendant(node, visited) is not None


def __get_valid_descendant(node, visited):
    for i in node.adjacent_nodes:
        counter = 0
        for j in visited:
            if i.value != j:
                counter += 1
        if counter == len(visited):
            return i
    return None
