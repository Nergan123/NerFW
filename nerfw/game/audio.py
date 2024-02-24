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

    def play(self, filename: str, repeat: bool = False):
        """
        Adds audio to html to be shown

        :param filename: Audio file to play
        :param repeat: If audio should be repeatable
        :return: None
        """

        file = filename.split("/")[-1]

        dir_folder = files("nerfw.server.build")
        self.logger.debug(dir_folder)
        # noinspection PyTypeChecker
        path = Path(dir_folder.joinpath(file))

        if not os.path.exists(path):
            if os.name == "nt":
                arg = ["copy", filename, str(path)]
            else:
                arg = ["cp", filename, str(path)]
            subprocess.call(arg)

        self.logger.debug(f"Adding {filename} to scene")
        self.recorder.scene.add_audio(f"{file}", repeatable=repeat)

    def stop_playing(self, filename: str):
        """
        Stops audio from playing

        :param filename: Audio file to stop
        :return: None
        """

        filename = filename.split("/")[-1]
        self.logger.debug(f"Stopping {filename}")
        self.recorder.scene.remove_audio(filename)
