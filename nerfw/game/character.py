from nerfw.helpers.logger import LoggerBase


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
        self.recorder.check(text)

    def hide(self):
        """
        Removes character img from scene
        :return: None
        """

        self.logger.info("Hiding")
        self.recorder.scene.remove_character_from_scene(self)

    def show(self):
        """
        Shows character on display
        :return: None
        """

        self.recorder.scene.add_character_to_scene(self)
