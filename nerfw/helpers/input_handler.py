from json import dumps
from nerfw.helpers.logger import LoggerBase


class InputHandler(LoggerBase):
    """Class responsible for input handling"""

    def __init__(self, current_line: str, prev_line: str):
        super().__init__()
        self.cookie = {
            "lines": {
                "current": {
                    "line": current_line,
                    "back": False,
                    "choices": {}
                },
                "previous": {
                    "line": prev_line,
                    "back": False,
                    "choices": {}
                }
            }
        }

    def set_choices(self, choices: dict):
        """
        Sets choices in current line
        :param choices: Dict
        :return: None
        """

        self.cookie["lines"]["current"]["choices"] = choices

    def get_current_line(self):
        """
        Function to set input params when forward

        :return:
        """

        output = self.cookie["lines"]["current"]

        return dumps(output)

    def get_prev_line(self):
        """
        Function to set input params when backwards

        :return:
        """
        output = self.cookie["lines"]["previous"]

        return dumps(output)

    def set_line(self, line: str):
        """
        Sets new line as current
        :param line: Str
        :return: None
        """

        self.cookie["lines"]["previous"] = self.cookie["lines"]["current"].copy()
        self.cookie["lines"]["current"]["line"] = line

    def reset(self):
        """
        Resets to default
        :return: None
        """

        self.cookie = {
            "lines": {
                "current": {
                    "line": "",
                    "back": False,
                    "choices": {}
                },
                "previous": {
                    "line": "",
                    "back": False,
                    "choices": {}
                }
            }
        }
