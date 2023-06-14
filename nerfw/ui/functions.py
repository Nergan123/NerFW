from enum import Enum


class Functions(Enum):
    """Lists available functions for js"""

    FORWARD = "ForwardFunction()"
    BACKWARD = "BackwardFunction()"
    REDIRECT_GAME = "window.location.href='/game'"
    REDIRECT_MAIN_PAGE = "window.location.href='/'"
    INPUT_SUBMIT = "submit"
    INPUT_TEXT = "text"
