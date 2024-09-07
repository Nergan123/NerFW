from fastapi import APIRouter
from starlette.responses import Response

from nerfw.inner import ui

ui_config_router = APIRouter(prefix="/ui", tags=["ui_config"])


@ui_config_router.get("/background", response_class=Response)
async def get_background():
    image_data, image_type = await ui.get_background()

    return Response(content=image_data, media_type=image_type)
