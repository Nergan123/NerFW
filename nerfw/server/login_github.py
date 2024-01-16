import os

from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv

from nerfw import LoggerBase


class LoginGithub(LoggerBase):
    """
    Login to GitHub.
    """

    def __init__(self, oauth: OAuth):
        super().__init__()
        client_id, client_secret = self._get_id_and_secret()
        self.github = oauth.register(
            name="github",
            client_id=client_id,
            client_secret=client_secret,
            access_token_url="https://github.com/login/oauth/access_token",
            access_token_params=None,
            authorize_url="https://github.com/login/oauth/authorize",
            authorize_params=None,
            api_base_url="https://api.github.com/",
            client_kwargs={"scope": "user:email"},
        )

    def login(self):
        """
        Login to GitHub.
        :return: None
        """

        self.logger.info("Logging in to GitHub...")

    @staticmethod
    def _get_id_and_secret():
        """
        Gets id and secret from GitHub.
        :return: Tuple of id and secret
        """

        load_dotenv()
        try:
            client_id = os.environ["CLIENT_ID"]
            client_secret = os.environ["CLIENT_SECRET"]
        except KeyError:
            raise KeyError("CLIENT_ID and CLIENT_SECRET not found in .env file") from KeyError

        return client_id, client_secret
