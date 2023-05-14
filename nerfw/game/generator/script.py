from nerfw.helpers import LoggerBase


class Script(LoggerBase):
    """
    Script class
    Contains script of the game
    """

    def __init__(self):
        super().__init__()
        self.game_script = {
            0: {}
        }

    def get_last(self):
        """
        Returns an id of the last element
        :return: ID
        """

        last_element = list(self.game_script.keys())[-1]
        self.logger.debug(f"Returning last element id: {last_element}")
        return last_element

    def get_script(self):
        """
        Returns a game script object
        :return: Script dict
        """

        return self.game_script

    def set_script(self, script: dict):
        """
        Sets a script object
        :param script: Script dict
        :return: None
        """

        self.logger.info("Script set")
        self.game_script = script
