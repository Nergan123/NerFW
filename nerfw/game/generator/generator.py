import json
import os.path

from nerfw.game.character_files.character import Character
from nerfw.game.generator.script import Script
from nerfw.helpers import LoggerBase


class Generator(LoggerBase):
    """Class to generate game script"""

    def __init__(self):
        super().__init__()
        self.logger.info("Generator")
        self.script = Script()

    def add_line(self, line: str, character: Character):
        """
        Adds line of dialogue to the script
        :param line: Dialogue line
        :param character: Character class
        :return: None
        """

        last_element = self.script.get_last()
        script = self.script.get_script()
        script[last_element + 1] = script[last_element].copy()
        script[last_element + 1]["line"] = {}
        script[last_element + 1]["line"]["name"] = character.name
        script[last_element + 1]["line"]["color"] = character.color
        script[last_element + 1]["line"]["text"] = line

        self.logger.info(f"Setting line: {line}")
        self.script.set_script(script)

    def generate(self):
        """
        Generates a full script file
        :return: Script dictionary
        """

        self.logger.info("Generated final script")

        if not os.path.isdir("game_script"):
            self.logger.info("Creating dir for script and files")
            os.mkdir("game_script")

        self.logger.info("Saving script to json file")
        with open("game_script/script.json", "w") as script_file:
            json.dump(self.script.get_script(), script_file)

        return self.script
