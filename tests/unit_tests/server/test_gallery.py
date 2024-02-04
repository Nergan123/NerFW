import unittest
import sqlite3
from unittest.mock import patch
from nerfw.server.gallery import Gallery


class TestGallery(unittest.TestCase):
    """
    TestGallery is a test suite for the Gallery class.
    It uses the unittest framework and the mock library for mocking dependencies.
    """

    # pylint: disable=arguments-differ
    @patch("nerfw.helpers.db_handler.DbHandler")
    @patch("nerfw.helpers.img_handler.ImageHandler")
    def setUp(self, mock_img_handler, mock_db_handler):
        """
        setUp is a special method that is run before each test.
        It sets up the test environment and mocks the dependencies of the Gallery class.

        :param mock_img_handler: A mock object for the ImageHandler class.
        :param mock_db_handler: A mock object for the DbHandler class.
        """
        self.gallery = Gallery()
        self.gallery.img_handler = mock_img_handler
        self.gallery.db = mock_db_handler

    def test_gallery_get_images_with_valid_username(self):
        """
        test_gallery_get_images_with_valid_username tests the
        get_images method of the Gallery class with a valid username.
        It checks if the correct list of images is returned when
        the get_images method is called with a valid username.
        """
        self.gallery.db.execute.return_value = [
            ("image1", "category1"),
            ("image2", "category2"),
        ]
        result = self.gallery.get_images("valid_username")
        self.assertEqual(result, [("image1", "category1"), ("image2", "category2")])

    def test_gallery_get_images_with_no_images(self):
        """
        test_gallery_get_images_with_no_images tests the get_images method
        of the Gallery class with a username that has no images.
        It checks if an empty list is returned when the get_images method
        is called with a username that has no images.
        """
        self.gallery.db.execute.return_value = []
        result = self.gallery.get_images("username_with_no_images")
        self.assertEqual(result, [])

    def test_gallery_get_images_with_invalid_username(self):
        """
        test_gallery_get_images_with_invalid_username tests the get_images
        method of the Gallery class with an invalid username.
        It checks if an OperationalError is raised when the get_images
        method is called with an invalid username.
        """
        self.gallery.db.execute.side_effect = sqlite3.OperationalError
        with self.assertRaises(sqlite3.OperationalError):
            self.gallery.get_images("invalid_username")


if __name__ == "__main__":
    unittest.main()
