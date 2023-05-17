from nerfw.game import Character


class Breaker(Exception):
    """Breaks the script execution and returns a line"""

    def __init__(self, line: str, character: Character):
        self.line = line
        self.name = character.name
        self.img = character.img
        self.color = character
        super().__init__(self.line)
