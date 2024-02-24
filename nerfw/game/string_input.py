from nerfw.helpers.logger import LoggerBase


class StringInput(LoggerBase):
    """
    Allows string input
    """

    def __init__(self, recorder=None, cookies=None, string=None, string_id=None):
        super().__init__()
        self.recorder = recorder
        self.string_name = string
        self.string_id = string_id
        self.answer = None
        self.cookies = cookies
        self.setup()

    def setup(self):
        """
        Sets up string from cookies

        :return: None
        """

        try:
            self.logger.debug(
                f"Found existing string: {self.cookies['stringInput'][str(self.string_id)]}"
            )
            self.answer = self.cookies["stringInput"][str(self.string_id)]
        except KeyError:
            self.answer = ""

    def make(self):
        """
        Displays or passes a string

        :return: string
        """

        self.recorder.check(f"{self.string_name}{self.string_id}")
        self.recorder.scene.remove_string_input()
        return self.answer

    def to_dict(self):
        """
        Converts obj to dict

        :return: dict
        """

        return {"id": self.string_id, "text": self.string_name}
