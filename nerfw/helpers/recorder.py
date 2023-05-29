from json import loads
from nerfw.game.scene import Scene
from nerfw.helpers import LoggerBase
from nerfw.helpers.breaker import Breaker


class Recorder(LoggerBase):
    """Class to track progress"""

    def __init__(self, last_line: str, scene: Scene):
        super().__init__()
        self.previous = loads(last_line)
        self.scene = scene
        self.report = False

    def check(self, line: str):
        """
        Checks if line is already encountered

        :param line: Checks the current line
        :return: None
        """

        if self.report or (self.previous["line"] == ""):
            self.report = False
            raise Breaker(line, self.scene)

        if line == self.previous["line"] and not self.previous["back"]:
            self.report = True

        if line == self.previous["line"] and self.previous["back"]:
            raise Breaker(line, self.scene)
