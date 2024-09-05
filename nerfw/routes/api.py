from fastapi import APIRouter

from nerfw.routes.authentication import auth_router

api_router = APIRouter(prefix="/api", tags=["api"])
api_router.include_router(auth_router)
