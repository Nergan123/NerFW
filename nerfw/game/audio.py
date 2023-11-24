import os
import subprocess
from importlib.resources import files
from pathlib import Path

from nerfw.helpers.logger import LoggerBase


class Audio(LoggerBase):
    """
    Class for audio control
    """

    def __init__(self, recorder=None):
        super().__init__()
        self.recorder = recorder

    def play(self, filename: str):
        """
        Adds audio to html to be shown
        :param filename: Audio file to play
        :return: None
        """

        file = filename.split("/")[-1]

        dir_folder = files("nerfw.server")
        self.logger.debug(dir_folder)
        path = Path(dir_folder.joinpath(file))

        if not os.path.exists(path):
            if os.name == 'nt':
                arg = ['copy', filename, str(path)]
            else:
                arg = ['cp', filename, str(path)]
            subprocess.call(arg)

        self.logger.debug(f"Adding {filename} to scene")
        self.recorder.scene.add_audio(f"{file}")
