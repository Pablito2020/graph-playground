from tree.Tree import Tree
from graphicsnode.Colors import Color
from graphicsnode.NodeDraw import NodeDraw
from graphics import *
from graphicsnode.Dimensions import Dimensions


class PaintTree:

    @staticmethod
    def paint_tree(win, tree: Tree):
        visited_nodes = []
        if not tree.is_empty():
            visited_nodes.append(tree.root)
            PaintTree.paint_tree_recursive(win, tree, Point(Dimensions.SCREEN_WIDTH.value / 2, 0 + Dimensions.CIRCLE_RADIUS.value * 2), visited_nodes)
        win.getMouse()
        win.close()

    # TODO: The positions are currently broken
    @staticmethod
    def paint_tree_recursive(win, tree: Tree, point: Point, visited_nodes):
        # Draw root node
        graphic_node = NodeDraw(Circle(point, Dimensions.CIRCLE_RADIUS.value), Text(point, tree.root), tree.root)
        graphic_node.circle.setFill(Color.RED.value)
        graphic_node.circle.draw(win)
        graphic_node.text.setTextColor(Color.BLACK.value)
        graphic_node.text.draw(win)

        # Draw lines to kids

        childs = PaintTree.get_no_visited_childs(tree, visited_nodes)
        initial_point = Point(point.getX(), point.getY() + Dimensions.CIRCLE_RADIUS.value)
        y_kids = point.getY() + 4 * Dimensions.CIRCLE_RADIUS.value
        start_x = Dimensions.CIRCLE_RADIUS.value
        number_of_childs = len(childs)
        if number_of_childs % 2 != 0:
            middle = Line(initial_point, Point(point.getX(), y_kids))
            middle.draw(win)
            number_of_childs -= 1
            start_x *= 2
        while number_of_childs > 0:
            line_1 = Line(initial_point, Point(point.getX() + start_x, y_kids - Dimensions.CIRCLE_RADIUS.value))
            line_2 = Line(initial_point, Point(point.getX() - start_x, y_kids - Dimensions.CIRCLE_RADIUS.value))
            number_of_childs -= 2
            start_x = start_x + 2 * Dimensions.CIRCLE_RADIUS.value
            line_1.draw(win)
            line_2.draw(win)
        for i in childs:
            visited_nodes.append(i.root)
        start = -start_x + 2 * Dimensions.CIRCLE_RADIUS.value
        for i in childs:
            PaintTree.paint_tree_recursive(win, i, Point(point.getX() + start, y_kids), visited_nodes)
            start += 2 * Dimensions.CIRCLE_RADIUS.value

    @staticmethod
    def get_no_visited_childs(tree, visited):
        childs = []
        for i in tree.descendants:
            if not PaintTree.already_visited(i.root, visited):
                childs.append(i)
        return childs

    @staticmethod
    def already_visited(root, visited_nodes):
        for i in visited_nodes:
            if root == i:
                return True
        return False
