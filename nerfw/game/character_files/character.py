from nerfw.helpers import LoggerBase


class Character(LoggerBase):
    """Class for character_files"""

    def __init__(self, recorder=None, name="Test name", img_path="/", color=(0, 0, 0)):
        super().__init__()
        self.recorder = recorder
        self.name = name
        self.img = img_path
        self.color = color

    def say(self, text="Sample text"):
        """
        Character will display text
        :param text: String to display
        :return: None
        """

        self.logger.info(f"Adding to script: {text}")
        self.recorder.check(text, self)
