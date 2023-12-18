import unittest
from unittest.mock import patch, mock_open

import jwt

from nerfw.server.token_handler import TokenHandler


class TokenHandlerTests(unittest.TestCase):
    """
    This class contains unit tests for the TokenHandler class.
    """

    def setUp(self):
        """
        This method is called before each test. It initializes the TokenHandler object.
        """
        self.token_handler = TokenHandler()

    # pylint: disable=unused-argument
    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data="test_key")
    def test_key_retrieval_success(self, mock_file, mock_exists):
        """
        This test checks if the key retrieval
        method successfully retrieves the key when the key file exists.
        """
        mock_exists.return_value = True
        self.assertEqual(self.token_handler.get_key(), "test_key")

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data="test_key")
    def test_key_generation_success(self, mock_file, mock_exists):
        """
        This test checks if the key generation method
        successfully generates a key when the key file does not exist.
        """
        mock_exists.return_value = False
        self.token_handler.generate_key()
        mock_file.assert_called_once_with("data/key.ner", "w")

    @patch("jwt.encode")
    def test_token_creation_success(self, mock_encode):
        """
        This test checks if the token creation method successfully creates a token.
        """
        mock_encode.return_value = "test_token"
        self.assertEqual(self.token_handler.create_token("test_user"), "test_token")

    @patch("jwt.decode")
    def test_token_verification_success(self, mock_decode):
        """
        This test checks if the token verification method successfully verifies a token.
        """
        mock_decode.return_value = {"login": "test_user", "created": "test_date"}
        self.assertEqual(
            self.token_handler.verify_token("test_token"),
            {"login": "test_user", "created": "test_date"},
        )

    @patch("jwt.decode")
    def test_token_verification_failure(self, mock_decode):
        """
        This test checks if the token verification method correctly identifies an expired token.
        """
        mock_decode.side_effect = jwt.ExpiredSignatureError
        self.assertFalse(self.token_handler.verify_token("test_token"))

    @patch("jwt.decode")
    def test_token_unlock_success(self, mock_decode):
        """
        This test checks if the token unlock method successfully unlocks a token.
        """
        mock_decode.return_value = {"login": "test_user", "created": "test_date"}
        self.assertEqual(
            self.token_handler.unlock_token("test_token"),
            {"login": "test_user", "created": "test_date"},
        )


if __name__ == "__main__":
    unittest.main()
