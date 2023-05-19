from nerfw.game import Character
from nerfw.helpers.recorder import Recorder
from nerfw.game.scene import Scene
from nerfw.helpers import LoggerBase


class Game(LoggerBase):
    """Class to create a game"""

    def __init__(self, last_line):
        super().__init__()
        self.scene = Scene()
        self._recorder = Recorder(last_line, self.scene)

    def create_character(self, name: str, img: str, color: (int, int, int)):
        """
        Generates a character_files class
        :param name: Name of the character_files
        :param img: Path to image file
        :param color: Color in rgb from 0 to 255
        :return: Character class
        """

        character = Character(self._recorder, name, img, color)
        return character
