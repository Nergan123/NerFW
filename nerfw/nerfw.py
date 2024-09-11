import os
from pathlib import Path

import uvicorn

from nerfw.app import app
from nerfw.handlers.game import GameHandler
from nerfw.handlers.ui import Ui


class NerFW:
    def __init__(self):
        self._generate_secret()
        self._load_secret()
        self.app = app
        self.ui = Ui()
        self.game = GameHandler()
        self.text = "Hello, World!"

    def run(self):
        uvicorn.run(self.app, host="0.0.0.0", port=8000)

    @staticmethod
    def _generate_secret():
        """
        Generates a secret key.

        :return: None
        """

        secret_path = Path(__file__).parent / "secret.key"
        if not secret_path.exists():
            with open(secret_path, "wb") as f:
                f.write(os.urandom(32))

    @staticmethod
    def _load_secret():
        """
        Loads the secret key.

        :return: None
        """

        secret_path = Path(__file__).parent / "secret.key"
        with open(secret_path, "rb") as f:
            os.environ["SECRET_KEY"] = str(f.read())
