from nerfw.game.scene import Scene


class Breaker(Exception):
    """Breaks the script execution and returns a line"""

    def __init__(self, line: str, scene: Scene):
        self.line = line
        self.scene = scene
        super().__init__(self.line)
