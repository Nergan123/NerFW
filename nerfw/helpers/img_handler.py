import base64

from nerfw.helpers.logger import LoggerBase


class ImageHandler(LoggerBase):
    """Class for handling images"""

    def __init__(self):
        super().__init__()
        self.logger.debug("Initialized")

    def convert_to_base64(self, img_path: str):
        """
        Converts img and returns base64

        :param img_path: Path to img file
        :return: Base64 encoded img
        """

        self.logger.info(f"Converting {img_path} to base64")
        with open(img_path, "rb") as img:
            encoded_image = base64.b64encode(img.read())

        return encoded_image.decode("utf-8")
