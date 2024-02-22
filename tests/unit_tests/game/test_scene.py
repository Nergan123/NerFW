import unittest
from unittest.mock import MagicMock
from nerfw.game.scene import Scene
from nerfw.game.character import Character
from nerfw.helpers.errors.character_not_found import CharacterNotFoundError


class SceneTest(unittest.TestCase):
    """
    This class contains unit tests for the Scene class in the nerfw.game.scene module.
    """

    def setUp(self):
        """
        This method sets up the necessary objects for the tests.
        It is called before each test method is executed.
        """
        self.scene = Scene()
        self.scene.img_handler = MagicMock()
        self.scene.img_handler.convert_to_base64.return_value = "base64_image"
        self.character = Character("recorder", "name", "img", "color", "pos")

    def test_background_setting(self):
        """
        This test checks if the background image is set correctly.
        """
        self.scene.set_background("img_path")
        self.assertEqual(self.scene.background, "base64_image")

    def test_character_addition_to_scene(self):
        """
        This test checks if a character is added to the scene correctly.
        """
        self.scene.add_character_to_scene(self.character)
        self.assertIn(self.character, self.scene.characters_to_show)

    def test_character_removal_from_scene(self):
        """
        This test checks if a character is removed from the scene correctly.
        """
        self.scene.add_character_to_scene(self.character)
        self.scene.remove_character_from_scene(self.character)
        self.assertNotIn(self.character, self.scene.characters_to_show)

    def test_character_removal_from_scene_character_not_found(self):
        """
        This test checks if the correct exception is raised
        when trying to remove a character that is not in the scene.
        """
        with self.assertRaises(CharacterNotFoundError):
            self.scene.remove_character_from_scene(self.character)

    def test_choice_addition_to_scene(self):
        """
        This test checks if a choice is added to the scene correctly.
        """
        choice = ["choice1", "choice2", "choice3"]
        self.scene.add_choice_to_scene(choice)
        self.assertEqual(self.scene.choice, choice)

    def test_choice_removal_from_scene(self):
        """
        This test checks if a choice is removed from the scene correctly.
        """
        choice = ["choice1", "choice2", "choice3"]
        self.scene.add_choice_to_scene(choice)
        self.scene.remove_choice_from_scene()
        self.assertIsNone(self.scene.choice)

    def test_audio_addition(self):
        """
        This test checks if an audio file is added to the scene correctly.
        """
        self.scene.add_audio("filename")
        self.assertEqual(self.scene.audio, [{"name": "filename", "repeatable": False}])


if __name__ == "__main__":
    unittest.main()
