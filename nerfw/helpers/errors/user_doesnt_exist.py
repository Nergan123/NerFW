class UserDoesntExist(Exception):
    """Raised when character can't be found"""

    def __init__(self, login: str):
        message = f"Can't find user '{login}'"
        super().__init__(message)
