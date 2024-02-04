import unittest
from unittest.mock import patch
from nerfw.server.login_default import LoginDefault
from nerfw.helpers.errors.password_mismatch import PasswordsMismatch
from nerfw.helpers.errors.user_doesnt_exist import UserDoesntExist


class LoginDefaultTests(unittest.TestCase):
    """
    This class contains unit tests for the LoginHandler class.
    """

    def setUp(self):
        """
        This method is called before each test. It initializes the LoginHandler object.
        """
        self.login_handler = LoginDefault()

    @patch("nerfw.helpers.db_handler.DbHandler.execute")
    def test_login_handler_login_user_doesnt_exist(self, mock_execute):
        """
        This test checks if the login method raises
        a UserDoesntExist exception when the user does not exist.
        """
        mock_execute.return_value = []
        with self.assertRaises(UserDoesntExist):
            self.login_handler.login(
                {"Login": "test_user", "Password": "test_password"}
            )

    @patch("nerfw.helpers.db_handler.DbHandler.execute")
    def test_login_handler_login_password_mismatch(self, mock_execute):
        """
        This test checks if the login method raises a
        PasswordsMismatch exception when the password is incorrect.
        """
        mock_execute.return_value = [("different_hashed_password", "salt")]
        with self.assertRaises(PasswordsMismatch):
            self.login_handler.login(
                {"Login": "test_user", "Password": "test_password"}
            )

    @patch("nerfw.server.password_manager.PasswordManager.register")
    def test_login_handler_register_success(self, mock_register):
        """
        This test checks if the register method
        calls the register method of the PasswordManager class.
        """
        self.login_handler.register(
            {
                "Login": "test_user",
                "Password": "test_password",
                "Repeat_password": "test_password",
            }
        )
        mock_register.assert_called_once_with(
            {
                "Login": "test_user",
                "Password": "test_password",
                "Repeat_password": "test_password",
            }
        )

    def test_login_handler_register_password_mismatch(self):
        """
        This test checks if the register method raises
        a PasswordsMismatch exception when the passwords do not match.
        """
        with self.assertRaises(PasswordsMismatch):
            self.login_handler.register(
                {
                    "Login": "test_user",
                    "Password": "test_password",
                    "Repeat_password": "different_test_password",
                }
            )


if __name__ == "__main__":
    unittest.main()
