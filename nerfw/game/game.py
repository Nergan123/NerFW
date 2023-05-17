from nerfw.game import Ui, Character
from nerfw.game.recorder import Recorder
from nerfw.helpers import LoggerBase


class Game(LoggerBase):
    """Class to create a game"""

    def __init__(self, last_line):
        super().__init__()
        self.ui = Ui()
        self.recorder = Recorder(last_line)

    def create_character(self, name: str, img: str, color: (int, int, int)):
        """
        Generates a character_files class
        :param name: Name of the character_files
        :param img: Path to image file
        :param color: Color in rgb from 0 to 255
        :return: Character class
        """

        character = Character(self.recorder, name, img, color)
        return character
