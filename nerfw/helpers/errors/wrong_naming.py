class WrongNamingFormatError(Exception):
    """Raised when character can't be found"""

    def __init__(self, name):
        message = f"Wrong formatting for '{name}'. Name's should not have any spaces"
        super().__init__(message)
