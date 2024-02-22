import unittest
import sqlite3
from unittest.mock import patch
from nerfw.game.unlock_scene import UnlockScene


class TestUnlockScene(unittest.TestCase):
    """
    TestUnlockScene is a test suite for the UnlockScene class.
    It uses the unittest framework and the mock library for mocking dependencies.
    """

    # pylint: disable=arguments-differ
    @patch("nerfw.helpers.db_handler.DbHandler")
    @patch("nerfw.helpers.img_handler.ImageHandler")
    def setUp(self, mock_img_handler, mock_db_handler):
        """
        setUp is a special method that is run before each test.
        It sets up the test environment and mocks the dependencies of the UnlockScene class.

        :param mock_img_handler: A mock object for the ImageHandler class.
        :param mock_db_handler: A mock object for the DbHandler class.
        """
        self.unlock_scene = UnlockScene()
        self.unlock_scene.img_handler = mock_img_handler
        self.unlock_scene.db = mock_db_handler

    def test_unlock_scene_with_valid_data(self):
        """
        test_unlock_scene_with_valid_data tests the unlock
        method of the UnlockScene class with valid data.
        It checks if the execute method of the DbHandler class
        is called once when the unlock method is called with valid data.
        """
        self.unlock_scene.img_handler.convert_to_base64.return_value = "base64image"
        self.unlock_scene.unlock("image_path", "username", "label", "category")
        self.unlock_scene.db.execute.assert_called_once()

    def test_unlock_scene_with_existing_scene(self):
        """
        test_unlock_scene_with_existing_scene tests the unlock
        method of the UnlockScene class with a scene that already exists in the database.
        It checks if the execute method of the DbHandler class
        is called once even if an IntegrityError is raised.
        """
        self.unlock_scene.img_handler.convert_to_base64.return_value = "base64image"
        self.unlock_scene.db.execute.side_effect = sqlite3.IntegrityError
        self.unlock_scene.unlock("image_path", "username", "label", "category")
        self.unlock_scene.db.execute.assert_called_once()

    def test_unlock_scene_with_invalid_image_path(self):
        """
        test_unlock_scene_with_invalid_image_path tests the unlock
        method of the UnlockScene class with an invalid image path.
        It checks if a FileNotFoundError is raised when the convert_to_base64
        method of the ImageHandler class is called with an invalid image path.
        """
        self.unlock_scene.img_handler.convert_to_base64.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            self.unlock_scene.unlock(
                "invalid_image_path", "username", "label", "category"
            )


if __name__ == "__main__":
    unittest.main()
