from factory.BFSFactory import BFSFactory
from factory.ColorFactory import ColorFactory
from factory.DFSFactory import DFSFactory
from factory.GraphFactory import GraphFactory
from structure.Graph import Graph


class Factory:

    @staticmethod
    def get_painting(option, graph: Graph):
        if option == "g":
            return GraphFactory(graph)
        if option == "b":
            return BFSFactory(graph)
        if option == "d":
            return DFSFactory(graph)
        if option == "c":
            return ColorFactory(graph)
        raise ValueError()

    @staticmethod
    def correct_option(option):
        option = option.lower()
        try:
            Factory.get_painting(option, Graph())
            return True
        except ValueError as e:
            return False




