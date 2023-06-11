class FunctionNotFound(Exception):
    """Raised when character can't be found"""

    def __init__(self, func):
        message = f"Can't find specified function '{repr(func)}'"
        super().__init__(message)
