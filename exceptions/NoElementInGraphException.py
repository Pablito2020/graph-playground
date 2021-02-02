class NoNodeInGraphException(Exception):

    def __init__(self):
        super(NoNodeInGraphException, self).__init__("No element inside the graph")
