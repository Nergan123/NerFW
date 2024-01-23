class UserNotAllowed(Exception):
    """
    Exception for user not allowed
    """
    def __init__(self, user_name: str):
        self.message = f"User {user_name} is not allowed"
        super().__init__(self.message)
