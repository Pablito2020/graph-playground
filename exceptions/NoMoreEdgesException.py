class NoMoreEdgesException(Exception):

    def __init__(self):
        super(NoMoreEdgesException, self).__init__("No more edges to add!")
