from nerfw.helpers import LoggerBase


class Character(LoggerBase):
    """Class for character"""

    def __init__(self, name="Test name"):
        super().__init__()
        self.name = name

    def say(self, text="Sample text"):
        """
        Character will display text
        :param text: String to display
        :return: string
        """

        self.logger.info(f"Displaying: {text}")
        return text
