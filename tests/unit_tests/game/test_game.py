import unittest
from unittest.mock import patch
from nerfw.game.game import Game


class GameTests(unittest.TestCase):
    """
    Unit test class for the Game class in the nerfw.game.game module.
    """

    def setUp(self):
        """
        Set up method for the test class. Initializes an instance of the Game class.
        """
        self.game = Game(last_line='{"line": "line1", "prev_line": "line0"}', username="user")

    def test_game_create_character(self):
        """
        Test case to verify that the create_character method correctly creates a Character instance.
        """
        character = self.game.create_character(
            "Test Character", "img_path", (255, 255, 255), (0, 0)
        )
        self.assertEqual(character.name, "Test Character")
        self.assertEqual(character.img, "img_path")
        self.assertEqual(character.color, (255, 255, 255))
        self.assertEqual(character.animation.current_x, 0)
        self.assertEqual(character.animation.current_y, 0)

    @patch("nerfw.game.scene.Scene.set_background")
    def test_game_set_background(self, mock_set_background):
        """
        Test case to verify that the set_background
        method correctly sets the background of the Scene instance.
        """
        self.game.set_background("background_img_path")
        mock_set_background.assert_called_once_with("background_img_path")

    @patch("nerfw.game.audio.Audio.play")
    def test_game_play_audio(self, mock_play):
        """
        Test case to verify that the play_audio method correctly plays an audio file.
        """
        self.game.play_audio("audio_file.mp3")
        mock_play.assert_called_once_with("audio_file.mp3", False)


if __name__ == "__main__":
    unittest.main()
