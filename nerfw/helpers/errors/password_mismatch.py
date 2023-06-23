class PasswordsMismatch(Exception):
    """Raised when passwords do not match"""

    def __init__(self):
        message = "Passwords do not match"
        super().__init__(message)
