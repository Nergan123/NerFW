import os.path

from nerfw.helpers.img_handler import ImageHandler

from nerfw.game.animation import Animations
from nerfw.helpers.logger import LoggerBase


class Character(LoggerBase):
    """Class for character_files"""

    # pylint: disable=too-many-arguments
    def __init__(self, recorder=None, name="Test name", img_path="/", color=(0, 0, 0), pos=(0, 0)):
        super().__init__()
        self.recorder = recorder
        self.name = name
        self.img = img_path
        self.img_handler = ImageHandler()
        self.color = color
        self.animation = Animations(pos[0], pos[1])
        self.img_scale = {
            "height": 100,
            "width": 100
        }

    def to_dict(self):
        """
        Converts to dict

        :return: dict
        """

        output = {
            "name": self.name,
            "color": self.color,
            "img": self.img_handler.convert_to_base64(self.img),
            "scale": self.img_scale,
            "css": self.animation.css
        }

        return output

    def say(self, text="Sample text"):
        """
        Character will display text

        :param text: String to display
        :return: None
        """

        self.logger.info(f"Adding to script: {text}")
        self.recorder.check(text, self.name, self.color)

    def hide(self):
        """
        Removes character img from scene

        :return: None
        """

        self.logger.info("Hiding")
        self.recorder.scene.remove_character_from_scene(self)

    def show(self):
        """
        Shows character on display

        :return: None
        """

        self.recorder.scene.add_character_to_scene(self)

    def scale(self, height: int, width: int):
        """
        Scales character

        :param height: Height of the character image in px
        :param width: Width of the character image in px
        :return: None
        """

        self.img_scale = {
            "height": f"{height}px",
            "width": f"{width}px"
        }

    def set_image(self, img_path: str):
        """
        Sets character image

        :param img_path: Path to image
        :return: None
        """

        if not os.path.exists(img_path):
            self.logger.error(f"Path {img_path} is a directory")
            raise FileNotFoundError(f"Path {img_path} is a directory")

        self.logger.debug(f"Setting img to {img_path}")
        self.img = img_path
