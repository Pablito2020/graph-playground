class NoMoreColorsException(Exception):

    def __init__(self):
        super(NoMoreColorsException, self).__init__("No more colors available")
