import unittest
from unittest.mock import patch, MagicMock
from nerfw.helpers.img_handler import ImageHandler


class ImageHandlerTests(unittest.TestCase):
    """
    Unit test class for the ImageHandler class in the nerfw.helpers.img_handler module.
    """

    def setUp(self):
        """
        Set up method for the test class. Initializes an instance of the ImageHandler class.
        """
        self.img_handler = ImageHandler()

    @patch("builtins.open", new_callable=MagicMock)
    def test_image_conversion_returns_base64(self, mock_open):
        """
        Test case to verify that the convert_to_base64
        method correctly converts an image file to a base64 string.
        """
        mock_open.return_value.__enter__.return_value.read.return_value = (
            b"test_image_data"
        )
        output = self.img_handler.convert_to_base64("img_path")
        expected_output = "dGVzdF9pbWFnZV9kYXRh"
        self.assertEqual(output, expected_output)

    @patch("builtins.open", new_callable=MagicMock)
    def test_image_conversion_handles_empty_file(self, mock_open):
        """
        Test case to verify that the convert_to_base64 method correctly handles an empty image file.
        """
        mock_open.return_value.__enter__.return_value.read.return_value = b""
        output = self.img_handler.convert_to_base64("img_path")
        expected_output = ""
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
