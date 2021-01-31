from files.Pairs import Pairs


class Parser:

    @staticmethod
    def parse(text):
        result = []
        vertex = text.split(";")
        for i in vertex:
            if len(i) > 0:  # TODO: Learn more about how the split method works
                current = i.split("(")
                actual_vertex = current[0]
                actual_others = current[1].replace(")", "")
                actual_final = actual_others.split(",")
                result.append(Pairs(actual_vertex, actual_final))
        return result
