from fastapi import APIRouter

from nerfw.handlers.login import LoginHandler, LoginResults
from nerfw.schemas.login_request import LoginRequest
from nerfw.schemas.responses import LoginResponse

auth_router = APIRouter(prefix="/auth", tags=["auth"])
handler = LoginHandler()


@auth_router.post(
    "/login",
    description="Login to the application.",
    summary="Login to the application.",
    response_description="Login response",
    response_model=LoginResponse,
)
async def login(request: LoginRequest):
    """
    Login endpoint.

    :param request: Login request
    :return: Login response
    """

    result, user = await handler.login(request)
    if result == LoginResults.USER_NOT_FOUND:
        return LoginResponse(message="User not found", statusCode=404)
    if result == LoginResults.INCORRECT_PASSWORD:
        return LoginResponse(message="Incorrect password", statusCode=401)
    if result == LoginResults.SUCCESS:
        token = await handler.sign_jwt(user)
        return LoginResponse(
            message="Login successful",
            success=True,
            statusCode=200,
            user=user,
            token=token,
        )
