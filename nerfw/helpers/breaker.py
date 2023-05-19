from nerfw.game import Character
from nerfw.game.scene import Scene


class Breaker(Exception):
    """Breaks the script execution and returns a line"""

    def __init__(self, line: str, character: Character, scene: Scene):
        self.line = line
        self.name = character.name
        self.img = character.img
        self.color = character
        self.scene = scene
        super().__init__(self.line)
