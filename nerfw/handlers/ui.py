import logging
from io import BytesIO
from pathlib import Path
from typing import Tuple

from PIL import Image, ImageDraw

from nerfw.handlers.util.singleton import Singleton


class Ui(metaclass=Singleton):
    """User interface for NERFW."""

    def __init__(self):
        self.background = None
        self._logger = logging.getLogger(self.__class__.__name__)

    async def get_background(self) -> Tuple[bytes, str]:
        """
        Get the background image.

        :return: Tuple of bytes and content type.
        """

        self._logger.info("Getting background image.")
        if self.background is None:
            self._logger.warning("No background image set.")
            return await self.create_default_background(), "image/png"

        image_type = self.background.suffix

        return self.background.read_bytes(), f"image/{image_type}"

    def set_background(self, image_path: str | Path):
        """
        Set the background image.

        :param image_path: Path to the image.
        :return: None
        """

        self._logger.info(f"Setting background image to {image_path}")
        if isinstance(image_path, str):
            self._logger.debug("Converting image path to Path object.")
            image_path = Path(image_path)

        self.background = image_path

    async def create_default_background(self) -> bytes:
        """
        Create a default background image.

        :return: Bytes of the default background color.
        """

        self._logger.info("Creating default background image.")
        image = Image.new("RGB", (200, 100), "white")
        draw = ImageDraw.Draw(image)
        hex_color = "#153950"
        draw.rectangle([0, 0, 200, 100], fill=hex_color)

        buffered = BytesIO()
        image.save(buffered, format="PNG")
        image_bytes = buffered.getvalue()

        return image_bytes
