from nerfw.game import Ui
from nerfw.game.generator.generator import Generator
from nerfw.helpers import LoggerBase
from nerfw.server.server import Server
from nerfw.game.character_files.character import Character


class NerFW(LoggerBase):
    """
    Main class for Ner framework
    """

    def __init__(self):
        super().__init__()
        self.generator = Generator()
        self.ui = Ui()

    def run(self, debug=False):
        """
        Runs a game
        :return: None
        """

        server = Server(self.generator.script)
        self.logger.info("Launching NerFW")
        server.run(debug=debug)

    def create_character(self, name: str, img: str, color: (int, int, int)):
        """
        Generates a character_files class
        :param name: Name of the character_files
        :param img: Path to image file
        :param color: Color in rgb from 0 to 255
        :return: Character class
        """

        character = Character(self.generator, name, img, color)
        return character
