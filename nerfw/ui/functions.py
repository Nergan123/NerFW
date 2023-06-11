from enum import Enum


class Functions(Enum):
    """Lists available functions for js"""

    FORWARD = "ForwardFunction()"
    BACKWARD = "BackwardFunction()"
    GAME = "window.location.href='/game'"
    REDIRECT_MAIN_PAGE = "window.location.href='/'"
