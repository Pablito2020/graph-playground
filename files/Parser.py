import re
from files.Pairs import Pairs
import string


class Parser:

    @staticmethod
    def parse(text):
        result = []
        vertex = text.split("|")
        for i in range(len(vertex)):
            vertex[i] = vertex[i].replace(" ", "")
            vertex[i] = vertex[i].replace("\n", "")
        for current in vertex:
            final = current.split(":")
            adjacency = final[1].split(",")
            result.append(Pairs(final[0], adjacency))
        return result
