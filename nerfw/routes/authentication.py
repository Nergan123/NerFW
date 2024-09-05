from fastapi import APIRouter

from nerfw.schemas.login_request import LoginRequest

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/login")
async def login(request: LoginRequest):
    pass
