import os
import subprocess

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

        if not os.path.exists(f"nerfw/server/static/{file}"):
            if os.name == 'nt':
                arg = ['copy', filename, f"nerfw/server/static/{file}"]
            else:
                arg = ['cp', filename, f"nerfw/server/static/{file}"]
            subprocess.call(arg)

        self.logger.debug(f"Adding {filename} to scene")
        self.recorder.scene.add_audio(f"{file}")
