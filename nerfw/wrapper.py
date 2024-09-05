from fastapi import FastAPI

from nerfw.handlers.game_handler import GameHandler


class Wrapper(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handler: GameHandler | None = None
