from files.Parser import Parser
from exceptions.NoMoreEdgesException import NoMoreEdgesException


class File:

    def __init__(self, name):
        file = open(name, "r")
        lines = file.read()
        self.info = Parser.parse(lines)
        self.current = 0

    def get_edge(self):
        if self.current >= len(self.info):
            raise NoMoreEdgesException()
        self.current += 1
        return self.info[self.current - 1]

    def has_more_edges_to_add(self):
        return self.current < len(self.info)
