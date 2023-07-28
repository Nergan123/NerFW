from nerfw.game.character import Character
from nerfw.game.choice import Choice
from nerfw.helpers.recorder import Recorder
from nerfw.game.scene import Scene
from nerfw.helpers.logger import LoggerBase


class Game(LoggerBase):
    """Class to create a game"""

    def __init__(self, last_line):
        super().__init__()
        self.scene = Scene()
        self._recorder = Recorder(last_line, self.scene)
        self._choice_count = 0

    def create_character(self, name: str, img: str, color: (int, int, int), pos: (int, int)):
        """
        Generates a character_files class
        :param name: Name of the character_files
        :param img: Path to image file
        :param color: Color in rgb from 0 to 255
        :param pos: Position of the character on screen in percent
        :return: Character class
        """

        character = Character(self._recorder, name, img, color, pos)
        return character

    def set_background(self, img_path: str):
        """
        Sets background to display
        :param img_path: Path to image file
        :return: None
        """

        self.logger.debug(f"Setting background to: {img_path}")
        self.scene.set_background(img_path)

    def choice(self, choices: list):
        """
        Makes a choice
        :param choices: List of options
        :return: returns a list with booleans representing answers
        """

        choice = Choice(self._recorder, choices, self._recorder.previous, self._choice_count)
        self._recorder.scene.add_choice_to_scene(choice)
        self._choice_count += 1
        answers = choice.make()

        return answers
