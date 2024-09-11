from nerfw.handlers.util.singleton import Singleton


class GameHandler(metaclass=Singleton):
    """Class for handling game logic"""

    def __init__(self):
        self.text = "Hello, World!"
