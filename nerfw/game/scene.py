from nerfw.game import Character
from nerfw.helpers.errors.character_not_found import CharacterNotFoundError
from nerfw.helpers.img_handler import ImageHandler
from nerfw.helpers import LoggerBase


class Scene(LoggerBase):
    """Class which creates a scene description"""

    def __init__(self):
        super().__init__()
        self.background = None
        self.characters_to_show = []
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
