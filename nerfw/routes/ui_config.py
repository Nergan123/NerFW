from fastapi import APIRouter
from starlette.responses import Response

from nerfw.handlers.ui import Ui

ui_config_router = APIRouter(prefix="/ui", tags=["ui_config"])
ui = Ui()


@ui_config_router.get(
    "/background",
    description="Get the background image for the game.",
    summary="Get the background image for the game.",
    response_description="Background image",
    response_class=Response,
)
async def get_background():
    image_data, image_type = await ui.get_background()

    return Response(content=image_data, media_type=image_type)
