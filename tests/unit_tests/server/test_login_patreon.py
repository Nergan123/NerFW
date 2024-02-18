import unittest
from unittest.mock import patch
from nerfw.server.login_patreon import LoginPatreon


class TestLoginPatreon(unittest.TestCase):
    """
    Unit test class for the LoginPatreon class in the nerfw.server.login_patreon module.
    """

    def setUp(self):
        """
        Set up method for the unit tests. Initializes an instance of the LoginPatreon class.
        """
        self.login_patreon = LoginPatreon()

    @patch("os.environ", {"CLIENT_ID": "test_id", "CLIENT_SECRET": "test_secret"})
    def test_get_id_and_secret(self):
        """
        Test case for the _get_id_and_secret method of the LoginPatreon class.
        This method should return the client ID and secret from the environment variables.
        """
        # pylint: disable=protected-access
        client_id, client_secret = self.login_patreon._get_id_and_secret()
        self.assertEqual(client_id, "test_id")
        self.assertEqual(client_secret, "test_secret")

    @patch("os.environ", {"CREATOR_TOKEN": "test_token"})
    def test_get_creator_token(self):
        """
        Test case for the get_creator_token method of the LoginPatreon class.
        This method should return the creator token from the environment variables.
        """
        creator_token = self.login_patreon.get_creator_token()
        self.assertEqual(creator_token, "test_token")

    def test_get_method(self):
        """
        Test case for the get_method method of the LoginPatreon class.
        This method should return the string "patreon".
        """
        method = self.login_patreon.get_method()
        self.assertEqual(method, "patreon")

    @patch("os.environ", {"CLIENT_ID": "test_id"})
    def test_get_additional_data(self):
        """
        Test case for the get_additional_data method of the LoginPatreon class.
        This method should return a dictionary with the client ID and redirect URL.
        """
        data = self.login_patreon.get_additional_data()
        self.assertEqual(
            data,
            {
                "clientId": "test_id",
                "redirectUrl": "http://127.0.0.1:5000/patreon/callback",
            },
        )


if __name__ == "__main__":
    unittest.main()
