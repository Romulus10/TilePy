class InvalidMapFileException(Exception):
    def __init__(self, message):
        """
        :param message: The text to display with the exception.
        :exception: Should _always_ be treated as a fatal exception.
        """
        Exception.__init__(self)
        self.message = message
