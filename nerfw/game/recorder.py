from nerfw.game import Character
from nerfw.helpers import LoggerBase
from nerfw.helpers.breaker import Breaker


class Recorder(LoggerBase):
    """Class to track progress"""

    def __init__(self, last_line):
        super().__init__()
        self.previous = last_line
        self.report = False

    def check(self, line: str, character: Character):
        """
        Checks if line is already encountered

        :param line: Checks the current line
        :param character: Character class
        :return: None
        """

        if self.report or (self.previous == ""):
            self.report = False
            raise Breaker(line, character)

        if line == self.previous:
            self.report = True
