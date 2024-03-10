import unittest
from unittest.mock import MagicMock, patch
from nerfw.game.character import Character


class CharacterTests(unittest.TestCase):
    """
    Unit test class for the Character class in the nerfw.login_register.character module.
    """

    def setUp(self):
        """
        Set up method for the test class. Initializes an instance of the Character class.
        """
        self.recorder_mock = MagicMock()
        self.character = Character(
            self.recorder_mock, "Test Character", "img_path", (255, 255, 255), (0, 0)
        )

    def test_character_to_dict(self):
        """
        Test case to verify that the to_dict method correctly
        converts a Character instance to a dictionary.
        """
        self.character.img_handler.convert_to_base64 = MagicMock(
            return_value="mocked_base64"
        )
        output = self.character.to_dict()
        expected_output = {
            "name": "Test Character",
            "color": (255, 255, 255),
            "img": "mocked_base64",
            "css": self.character.animation.css,
            "scale": {"height": 100, "width": 100},
        }
        self.assertEqual(output, expected_output)

    def test_character_say(self):
        """
        Test case to verify that the say method
        correctly calls the check method of the recorder mock.
        """
        self.character.say("Hello, world!")
        self.recorder_mock.check.assert_called_once_with(
            "Hello, world!", "Test Character", (255, 255, 255)
        )

    def test_character_hide(self):
        """
        Test case to verify that the hide method correctly
        calls the remove_character_from_scene method of the scene mock.
        """
        self.character.hide()
        self.recorder_mock.scene.remove_character_from_scene.assert_called_once_with(
            self.character
        )

    def test_character_show(self):
        """
        Test case to verify that the show method correctly
        calls the add_character_to_scene method of the scene mock.
        """
        self.character.show()
        self.recorder_mock.scene.add_character_to_scene.assert_called_once_with(
            self.character
        )

    @patch("os.path.exists")
    def image_path_exists(self, mock_exists):
        """
        Test case to verify that the set_image method correctly sets the image path
        when the provided path exists.

        This method uses the unittest.mock.patch decorator to mock the os.path.exists
        function, making it always return True. This allows us to simulate a scenario
        where the image path provided to the set_image method exists.

        The set_image method is then called with a valid image path, and we assert that
        the logger's debug method was called with the correct message, and that the
        character's img attribute was set to the provided path.
        """
        mock_exists.return_value = True
        self.character.set_image("valid/path/to/image.png")
        self.character.logger.debug.assert_called_with(
            "Setting img to valid/path/to/image.png"
        )
        self.assertEqual(self.character.img, "valid/path/to/image.png")

    @patch("os.path.exists")
    def image_path_does_not_exist(self, mock_exists):
        """
        Test case to verify that the set_image method raises a FileNotFoundError
        when the provided path does not exist.

        This method uses the unittest.mock.patch decorator to mock the os.path.exists
        function, making it always return False. This allows us to simulate a scenario
        where the image path provided to the set_image method does not exist.

        The set_image method is then called with an invalid image path, and we assert that
        a FileNotFoundError is raised, and that the logger's error method was called with
        the correct message.
        """
        mock_exists.return_value = False
        with self.assertRaises(FileNotFoundError):
            self.character.set_image("invalid/path/to/image.png")
        self.character.logger.error.assert_called_with(
            "Path invalid/path/to/image.png is a directory"
        )


if __name__ == "__main__":
    unittest.main()
