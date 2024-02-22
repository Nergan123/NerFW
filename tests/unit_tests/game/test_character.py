import unittest
from unittest.mock import MagicMock
from nerfw.game.character import Character


class CharacterTests(unittest.TestCase):
    """
    Unit test class for the Character class in the nerfw.game.character module.
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


if __name__ == "__main__":
    unittest.main()
