class Tree:

    def __init__(self, value):
        self.descendants = []
        self.root = value

    def add_descendant(self, tree):
        self.descendants.append(tree)

    def get_tree(self, value):
        return self.__get_tree_recursive(self, value, [])

    def __get_tree_recursive(self, tree, value, visited):
        if tree.root == value:
            return tree
        if value in visited:
            return None
        visited.append(tree.root)
        for i in tree.descendants:
            current = self.__get_tree_recursive(i, value, visited)
            if current is not None:
                return current

    def no_descendants(self):
        return len(self.descendants) == 0

    def height(self):
        return self.__height_recursive(self, [])

    def __height_recursive(self, tree, visited):
        if tree.no_descendants():
            return 1
        if tree.root in visited:
            return 0
        visited.append(tree.root)
        counter = []
        for i in tree.descendants:
            counter.append(self.__height_recursive(i, visited))
        height = max(counter)
        return height + 1

