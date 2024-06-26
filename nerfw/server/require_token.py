from functools import wraps

from flask import request, redirect

from nerfw.server.token_handler import TokenHandler


def require_token(func):
    """
    Decorator to check if token is available

    :param func: Function to check
    :return: Wrapper
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get("token")
        handler = TokenHandler()
        answer = handler.verify_token(token)
        if not answer:
            response = redirect("/login")
            response.set_cookie("token", "", expires=0)
            return response
        return func(*args, *kwargs)

    return wrapper
