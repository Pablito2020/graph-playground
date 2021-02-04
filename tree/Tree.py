class Tree:

    def __init__(self, value):
        self.descendants = []
        self.root = value

    def add_descendant(self, tree):
        self.descendants.append(tree)

    def get_tree(self, value):
        return self.get_tree_recursive(self, value, [])

    def get_tree_recursive(self, tree, value, visited):
        if tree.root == value:
            return tree
        if value in visited:
            return None
        visited.append(tree.root)
        for i in tree.descendants:
            current = self.get_tree_recursive(i, value, visited)
            if current is not None:
                return current

    def is_empty(self):
        return len(self.descendants) == 0
