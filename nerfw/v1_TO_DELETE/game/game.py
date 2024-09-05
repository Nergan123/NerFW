from nerfw.game.audio import Audio
from nerfw.game.character import Character
from nerfw.game.choice import Choice
from nerfw.game.string_input import StringInput
from nerfw.game.unlock_scene import UnlockScene
from nerfw.helpers.recorder import Recorder
from nerfw.game.scene import Scene
from nerfw.helpers.logger import LoggerBase


class Game(LoggerBase):
    """Class to create a login_register"""

    def __init__(self, *args, **kwargs):
        _ = args
        username = kwargs.get("username")
        last_line = kwargs.get("last_line")
        super().__init__()
        self._username = username
        self.scene = Scene()
        self.unlocker = UnlockScene()
        self._recorder = Recorder(last_line, self.scene)
        self._audio = Audio(self._recorder)
        self._choice_count = 0
        self._string_count = 0

    def create_character(
        self, name: str, img: str, color: (int, int, int), pos: (int, int)
    ):
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

        choice = Choice(
            self._recorder, choices, self._recorder.previous, self._choice_count
        )
        self._recorder.scene.add_choice_to_scene(choice)
        self._choice_count += 1
        answers = choice.make()

        return answers

    def string_input(self, string_name: str):
        """
        Allows string input

        :param string_name: Name of the variable to display
        :return: Answer from user
        """

        string_input = StringInput(
            self._recorder, self._recorder.previous, string_name, self._string_count
        )
        self._recorder.scene.add_string_input(string_input)
        self._string_count += 1
        answer = string_input.make()

        return answer

    def play_audio(self, filename: str, repeat: bool = False):
        """
        Plays audio

        :param filename: File to play
        :param repeat: Whether to repeat audio or not
        :return: None
        """

        self._audio.play(filename, repeat)

    def stop_audio(self, filename: str):
        """
        Stops audio

        :param filename: File to stop
        :return: None
        """

        self._audio.stop_playing(filename)

    def unlock_scene(self, img_path: str, label: str, category: str = None):
        """
        Unlocks scene

        :param img_path: Path to image file
        :param category: Category of the scene
        :param label: Label of the scene. Should be unique
        :return: None
        """

        self.unlocker.unlock(img_path, self._username, label, category)
        self.logger.info(f"{self._username} Unlocked scene: {img_path}")
