import uvicorn

from nerfw.app import app
from nerfw.handlers.game_handler import GameHandler


class NerFW:
    def __init__(self):
        self.app = app
        self.text = "Hello, World!"
        app.handler = GameHandler()

    def run(self):
        uvicorn.run(self.app, host="0.0.0.0", port=8000)
