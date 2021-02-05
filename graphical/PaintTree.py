from structure.Tree import Tree
from colors.Color import StockColor
from graphical.NodeDraw import NodeDraw
from graphics import *
from graphical.Dimensions import Dimensions


class PaintTree:

    @staticmethod
    def paint_tree(win, tree: Tree):
        visited_nodes = []
        if not tree.no_descendants():
            visited_nodes.append(tree.root)
            PaintTree.paint_tree_recursive(win, tree,
                                           Point(Dimensions.SCREEN_WIDTH.value / 2, Dimensions.CIRCLE_RADIUS.value), 0,
                                           Dimensions.SCREEN_WIDTH.value, visited_nodes)
        win.getMouse()
        win.close()

    @staticmethod
    def paint_tree_recursive(win, tree: Tree, point: Point, x_min, x_max, visited_nodes):
        # Draw root node
        graphic_node = NodeDraw(Circle(point, Dimensions.CIRCLE_RADIUS.value), Text(point, tree.root), tree.root)
        graphic_node.circle.setFill(StockColor.NULL_COLOR.value.first)
        graphic_node.circle.draw(win)
        graphic_node.text.setTextColor(StockColor.NULL_COLOR.value.second)
        graphic_node.text.draw(win)

        # Draw lines to kids
        childs = PaintTree.get_no_visited_childs(tree, visited_nodes)
        initial_point = Point(point.getX(), point.getY() + Dimensions.CIRCLE_RADIUS.value)
        y_kids = point.getY() + 2 * Dimensions.CIRCLE_RADIUS.value
        number_of_childs = len(childs)
        if number_of_childs == 0:
            return
        available_screen = (x_max - x_min) / number_of_childs
        current = x_min
        for i in range(number_of_childs):
            coordenates = Point((current + available_screen) / 2, y_kids)
            current += 2 * available_screen
            line = Line(initial_point, coordenates)
            line.draw(win)
        for i in childs:
            visited_nodes.append(i.root)
        current = x_min
        for i in childs:
            PaintTree.paint_tree_recursive(win, i, Point((current + available_screen) / 2,
                                                         y_kids + Dimensions.CIRCLE_RADIUS.value), current,
                                           current + available_screen, visited_nodes)
            current += 2 * available_screen

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
