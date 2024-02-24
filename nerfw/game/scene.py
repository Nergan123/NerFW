from nerfw.game.character import Character
from nerfw.game.string_input import StringInput
from nerfw.helpers.errors.character_not_found import CharacterNotFoundError
from nerfw.helpers.img_handler import ImageHandler
from nerfw.helpers.logger import LoggerBase


class Scene(LoggerBase):
    """Class which creates a scene description"""

    def __init__(self):
        super().__init__()
        self.background = None
        self.characters_to_show = []
        self.choice = None
        self.string_input = None
        self.audio = []
        self.name = ""
        self.color = ()
        self.img_handler = ImageHandler()

    def set_background(self, img_file: str):
        """
        Sets background

        :param img_file:
        :return: None
        """

        self.logger.info(f"Setting Background to {img_file}")
        self.background = self.img_handler.convert_to_base64(img_file)

    def add_character_to_scene(self, character: Character):
        """
        Adds character to the displayed scene

        :param character: Character class to be shown
        :return: None
        """

        if character not in self.characters_to_show:
            self.logger.info(f"Adding to display: {character.name}")
            self.characters_to_show.append(character)

    def remove_character_from_scene(self, character: Character):
        """
        Removes character from display

        :param character: Character class to be removed
        :return: None
        """

        if character in self.characters_to_show:
            self.characters_to_show.remove(character)
        else:
            raise CharacterNotFoundError(character)

    def add_choice_to_scene(self, choice):
        """
        Adds choice to be displayed

        :param choice: Choice object
        :return: None
        """

        self.choice = choice
        self.logger.debug(f"Setting choice to: {choice}")

    def remove_choice_from_scene(self):
        """
        Removes choice from object

        :return: None
        """

        self.logger.debug("Removing choice from scene object")
        self.choice = None

    def add_audio(self, filename: str, repeatable: bool = False):
        """
        Adds audio to self

        :param filename: Audio file name
        :param repeatable: If audio should be repeatable
        :return: None
        """

        self.logger.debug(f"Added {filename}")
        file_info = {"name": filename, "repeatable": repeatable}
        self.audio.append(file_info)

    def remove_audio(self, filename: str):
        """
        Removes audio from self

        :param filename: Audio file name
        :return: None
        """

        self.logger.debug(f"Removed {filename}")
        self.audio = [file for file in self.audio if file["name"] != filename]

    def add_string_input(self, string_input: StringInput):
        """
        Adds string input to self

        :param string_input: String input object
        :return: None
        """

        self.logger.debug(f"Added {string_input}")
        self.string_input = string_input

    def remove_string_input(self):
        """
        Removes string input from self

        :return: None
        """

        self.logger.debug("Removed string input")
        self.string_input = None
