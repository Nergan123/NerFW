class UserAlreadyRegistered(Exception):
    """Raised when User is already exists"""

    def __init__(self, login: str):
        message = f"User '{login}' already exists"
        super().__init__(message)
