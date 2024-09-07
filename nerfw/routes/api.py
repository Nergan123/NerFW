from fastapi import APIRouter

from nerfw.routes.authentication import auth_router
from nerfw.routes.ui_config import ui_config_router

api_router = APIRouter(prefix="/api", tags=["api"])
api_router.include_router(auth_router)
api_router.include_router(ui_config_router)
