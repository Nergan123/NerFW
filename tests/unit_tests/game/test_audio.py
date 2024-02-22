import os
import unittest
from importlib.resources import files
from pathlib import Path
from unittest.mock import MagicMock, patch
from nerfw.game.audio import Audio


class AudioTests(unittest.TestCase):
    """
    Unit test class for the Audio class in the nerfw.game.audio module.
    """

    # pylint: disable=unused-argument
    def setUp(self):
        """
        Set up method for the test class. Initializes an instance of the Audio class.
        """
        dir_folder = files("nerfw.server")
        path = Path(dir_folder.joinpath("build"))
        if not os.path.exists(path):
            os.mkdir(path)
        self.recorder_mock = MagicMock()
        self.audio = Audio(self.recorder_mock)

    @patch("os.path.exists", return_value=True)
    def test_audio_play_existing_file(self, exists_mock):
        """
        Test case to verify that the play method correctly plays an existing audio file.
        """
        self.audio.play("existing_file.mp3")
        self.recorder_mock.scene.add_audio.assert_called_once_with(
            "existing_file.mp3", repeatable=False
        )

    @patch("os.path.exists", return_value=False)
    @patch("subprocess.call")
    def test_audio_play_non_existing_file(self, call_mock, exists_mock):
        """
        Test case to verify that the play method correctly handles a non-existing audio file.
        """
        self.audio.play("non_existing_file.mp3")
        call_mock.assert_called_once()
        self.recorder_mock.scene.add_audio.assert_called_once_with(
            "non_existing_file.mp3", repeatable=False
        )


if __name__ == "__main__":
    unittest.main()
