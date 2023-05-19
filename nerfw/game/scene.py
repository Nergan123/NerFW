from nerfw.helpers.img_handler import ImageHandler
from nerfw.helpers import LoggerBase


class Scene(LoggerBase):
    """Class which creates a scene description"""

    def __init__(self):
        super().__init__()
        self.background = None
        self.img_handler = ImageHandler()

    def set_background(self, img_file: str):
        """
        Sets background
        :param img_file:
        :return: None
        """

        self.logger.info(f"Setting Background to {img_file}")
        self.background = self.img_handler.convert_to_base64(img_file)
