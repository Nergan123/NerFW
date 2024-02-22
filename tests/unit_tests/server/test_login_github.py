import os
import unittest
from unittest.mock import patch, MagicMock
from authlib.integrations.flask_client import OAuth
from nerfw.server.login_github import LoginGithub


class TestLoginGithub(unittest.TestCase):
    """
    Unit tests for the LoginGithub class.
    """

    @patch("os.environ", {"CLIENT_ID": "test_id", "CLIENT_SECRET": "test_secret"})
    def test_login_github_initialization(self):
        """
        Test the initialization of the LoginGithub class.
        It checks if the OAuth client is registered with the correct parameters.
        """
        oauth = MagicMock(spec=OAuth)
        _ = LoginGithub(oauth)
        oauth.register.assert_called_once_with(
            name="github",
            client_id="test_id",
            client_secret="test_secret",
            access_token_url="https://github.com/login/oauth/access_token",
            access_token_params=None,
            authorize_url="https://github.com/login/oauth/authorize",
            authorize_params=None,
            api_base_url="https://api.github.com/",
            client_kwargs={"scope": "user:email"},
        )

    @patch.dict(os.environ, {"CLIENT_ID": "", "CLIENT_SECRET": "test_secret"})
    def test_login_github_initialization_missing_client_id(self):
        """
        Test the initialization of the LoginGithub class without a client ID.
        It checks if a KeyError is raised when the client ID is missing.
        """
        oauth = MagicMock(spec=OAuth)
        with self.assertRaises(KeyError):
            LoginGithub(oauth)

    @patch("os.environ", {"CLIENT_ID": "test_id", "CLIENT_SECRET": ""})
    def test_login_github_initialization_missing_client_secret(self):
        """
        Test the initialization of the LoginGithub class without a client secret.
        It checks if a KeyError is raised when the client secret is missing.
        """
        oauth = MagicMock(spec=OAuth)
        with self.assertRaises(KeyError):
            LoginGithub(oauth)

    @patch("os.environ", {"CLIENT_ID": "test_id", "CLIENT_SECRET": "test_secret"})
    def test_login_github_get_method(self):
        """
        Test the get_method function of the LoginGithub class.
        It checks if the returned method is 'github'.
        """
        oauth = MagicMock(spec=OAuth)
        login_github = LoginGithub(oauth)
        self.assertEqual(login_github.get_method(), "github")

    @patch("os.environ", {"CLIENT_ID": "test_id", "CLIENT_SECRET": "test_secret"})
    def test_login_github_get_additional_data(self):
        """
        Test the get_additional_data function of the LoginGithub class.
        It checks if the returned data contains the client ID.
        """
        oauth = MagicMock(spec=OAuth)
        login_github = LoginGithub(oauth)
        self.assertEqual(login_github.get_additional_data(), {"clientId": "test_id"})

    @patch.dict(os.environ, {"CLIENT_ID": "", "CLIENT_SECRET": "test_secret"})
    def test_login_github_get_additional_data_missing_client_id(self):
        """
        Test the get_additional_data function of the LoginGithub class without a client ID.
        It checks if a KeyError is raised when the client ID is missing.
        """
        oauth = MagicMock(spec=OAuth)
        with self.assertRaises(KeyError):
            login_github = LoginGithub(oauth)
            login_github.get_additional_data()


if __name__ == "__main__":
    unittest.main()
