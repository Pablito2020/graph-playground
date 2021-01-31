class no_node_in_graph_exception(Exception):

    def __init__(self):
        super(no_node_in_graph_exception, self).__init__("No element inside the graph")
