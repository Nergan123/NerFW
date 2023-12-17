import sqlite3
import unittest
from unittest.mock import patch, MagicMock
from nerfw.server.password_manager import PasswordManager
from nerfw.helpers.errors.user_already_registered import UserAlreadyRegistered
from nerfw.helpers.db_handler import DbHandler


class PasswordManagerTest(unittest.TestCase):
    """
    This class contains unit tests for the PasswordManager
    class in the nerfw.server.password_manager module.
    """

    def setUp(self):
        """
        This method sets up the necessary objects for the tests.
        It is called before each test method is executed.
        """
        self.db = MagicMock(spec=DbHandler)
        self.password_manager = PasswordManager(self.db)

    @patch("nerfw.server.password_manager.PasswordManager.encrypt")
    def test_successful_registration(self, mock_encrypt):
        """
        This test checks if the registration is successful when the user does not already exist.
        """
        mock_encrypt.return_value = ("hashed_password", "salt")
        self.db.execute.return_value = None
        data = {"Login": "new_user", "Password": "new_password"}

        self.password_manager.register(data)

        mock_encrypt.assert_called_once_with("new_password")
        self.db.execute.assert_called_once()

    @patch("nerfw.server.password_manager.PasswordManager.encrypt")
    def test_unsuccessful_registration_user_already_exists(self, mock_encrypt):
        """
        This test checks if the registration fails when the user already exists.
        """
        mock_encrypt.return_value = ("hashed_password", "salt")
        self.db.execute.side_effect = sqlite3.IntegrityError
        data = {"Login": "existing_user", "Password": "test_password"}

        with self.assertRaises(UserAlreadyRegistered):
            self.password_manager.register(data)

        mock_encrypt.assert_called_once_with("test_password")
        self.db.execute.assert_called_once()

    def test_password_encryption(self):
        """
        This test checks if the password encryption is working correctly.
        """
        password = "test_password"
        hashed, salt = self.password_manager.encrypt(password)

        self.assertEqual(len(hashed), 64)  # SHA-256 produces a 64 character hash
        self.assertEqual(len(salt), 25)  # Salt length is 25 as per the encrypt method

    def test_password_encryption_with_provided_salt(self):
        """
        This test checks if the password encryption is working correctly when a salt is provided.
        """
        password = "test_password"
        provided_salt = "random_salt"
        hashed, salt = self.password_manager.encrypt(password, provided_salt)

        self.assertEqual(len(hashed), 64)  # SHA-256 produces a 64 character hash
        self.assertEqual(
            salt, provided_salt
        )  # Returned salt should be the same as the provided salt


if __name__ == "__main__":
    unittest.main()
