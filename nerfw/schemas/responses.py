from pydantic import BaseModel

from nerfw.schemas.user import User


class LoginResponse(BaseModel):
    token: str | None = None
    user: User | None = None
    message: str = ""
    success: bool = False
    statusCode: int = 400
