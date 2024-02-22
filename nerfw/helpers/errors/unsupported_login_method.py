class UnsupportedLoginMethodError(Exception):
    """
    Exception raised when a login method is not supported.
    """
    def __init__(self, method: str):
        message = f"Unsupported login method: {method}"
        super().__init__(message)
