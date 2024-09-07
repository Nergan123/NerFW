import logging
from pathlib import Path
from typing import Tuple


class Ui:
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
            return b"", "image/png"

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
