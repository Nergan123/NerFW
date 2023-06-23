from json import dumps
from nerfw.helpers.logger import LoggerBase


class InputHandler(LoggerBase):
    """Class responsible for input handling"""

    def __init__(self, current_line: str, prev_line: str):
        super().__init__()
        self.current_line = current_line
        self.prev_line = prev_line

    def get_current_line(self):
        """
        Function to set input params when forward

        :return:
        """
        output = {
            "line": self.current_line,
            "back": False
        }

        return dumps(output)

    def get_prev_line(self):
        """
        Function to set input params when backwards

        :return:
        """
        output = {
            "line": self.prev_line,
            "back": True
        }

        return dumps(output)

    def set_line(self, line: str):
        """
        Sets new line as current
        :param line: Str
        :return: None
        """

        self.prev_line = self.current_line
        self.current_line = line

    def reset(self):
        """
        Resets to default
        :return: None
        """

        self.prev_line = ""
        self.current_line = ""
