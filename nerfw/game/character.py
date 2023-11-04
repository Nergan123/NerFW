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

    def to_dict(self):
        """
        Converts to dict

        :return: dict
        """

        output = {
            "name": self.name,
            "color": self.color,
            "img": self.img_handler.convert_to_base64(self.img),
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
        self.recorder.check(text, self.name)
        self.animation.css = ""

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
