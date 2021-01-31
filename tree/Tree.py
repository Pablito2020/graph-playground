class Tree:

    def __init__(self, value):
        self.descendants = []
        self.root = value

    def add_descendant(self, tree):
        self.descendants.append(tree)
