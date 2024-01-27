import unittest
from unittest.mock import patch, MagicMock
from nerfw.helpers.deconstructor import Deconstructor
from nerfw.helpers.breaker import Breaker
from nerfw.game.scene import Scene
from nerfw.game.character import Character


class DeconstructorTests(unittest.TestCase):
    """
    Unit test class for the Deconstructor class in the nerfw.helpers.deconstructor module.
    """

    def setUp(self):
        """
        Set up method for the test class.
        Initializes an instance of the Deconstructor class and a Breaker instance.
        """
        self.deconstructor = Deconstructor()
        self.breaker = Breaker("Test line", Scene())

    def test_deconstructor_initialization(self):
        """
        Test case to verify that the Deconstructor class is correctly initialized.
        """
        self.assertIsInstance(self.deconstructor, Deconstructor)

    @patch("nerfw.helpers.deconstructor.ImageHandler.convert_to_base64")
    def test_deconstructor_deconstruct_no_choice(self, mock_convert_to_base64):
        """
        Test case to verify that the deconstruct
        method correctly deconstructs a Breaker instance without a choice.
        """
        mock_convert_to_base64.return_value = "base64"
        self.breaker.scene.characters_to_show = [
            Character("Test Character", "img_path", (255, 255, 255), (0, 0, 0))
        ]
        self.breaker.scene.string_input = MagicMock()
        output = self.deconstructor.deconstruct(self.breaker)
        expected_output = {
            "background": self.breaker.scene.background,
            "characters": [
                character.to_dict()
                for character in self.breaker.scene.characters_to_show
            ],
            "text": self.breaker.line,
            "stringInput": self.breaker.scene.string_input.to_dict(),
            "name": self.breaker.scene.name,
            "color": self.breaker.scene.color,
            "choice": {},
            "audio": self.breaker.scene.audio,
        }
        self.assertEqual(output, expected_output)

    @patch("nerfw.helpers.deconstructor.ImageHandler.convert_to_base64")
    def test_deconstructor_deconstruct_with_choice(self, mock_convert_to_base64):
        """
        Test case to verify that the deconstruct
        method correctly deconstructs a Breaker instance with a choice.
        """
        mock_convert_to_base64.return_value = "base64"
        self.breaker.scene.characters_to_show = [
            Character("Test Character", "img_path", (255, 255, 255), (0, 0, 0))
        ]
        self.breaker.scene.choice = MagicMock()
        self.breaker.scene.string_input = MagicMock()
        output = self.deconstructor.deconstruct(self.breaker)
        expected_output = {
            "background": self.breaker.scene.background,
            "characters": [
                character.to_dict()
                for character in self.breaker.scene.characters_to_show
            ],
            "text": self.breaker.line,
            "stringInput": self.breaker.scene.string_input.to_dict(),
            "name": self.breaker.scene.name,
            "color": self.breaker.scene.color,
            "choice": self.breaker.scene.choice.to_dict(),
            "audio": self.breaker.scene.audio,
        }
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
