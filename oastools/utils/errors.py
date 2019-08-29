class Error(Exception):
    def __init__(self, basemessage="Unspecified Error", message=""):
        self.basemessage = basemessage
        self.message = message
        super().__init__(basemessage, message)


class NotImplementedError(Error):
    """An error to indicate that the requested operation has not yet been implemented
    """

    def __init__(self, message=""):
        super().__init__("This feature has not yet been implemented.", message)


class ParseError(Error):
    def __init__(self, basemessage='ParserError', message=''):
        super().__init__(basemessage=basemessage, message=message)
