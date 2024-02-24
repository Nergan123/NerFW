import os

import requests
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
from flask import make_response, redirect, request

from nerfw.helpers.errors.user_not_allowed import UserNotAllowed
from nerfw.helpers.login_base import LoginBaseClass
from nerfw.server.token_handler import TokenHandler


class LoginGithub(LoginBaseClass):
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
        self.token_handler = TokenHandler()

    def login(self):
        """
        Login to GitHub.

        :return: JWT token
        """

        self.logger.info("Authorizing GitHub login...")
        request_token = request.args.get("code")
        access_token = self._get_access_token(request_token)
        user_data = self._get_user_data(access_token)

        if not self.check_user_allowed(user_data["login"]):
            raise UserNotAllowed(user_data["login"])

        jwt_token = self.token_handler.create_token(user_data["login"])

        return jwt_token

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
            raise KeyError(
                "CLIENT_ID and CLIENT_SECRET not found in .env file"
            ) from KeyError

        if client_id == "" or client_secret == "":
            raise KeyError("CLIENT_ID or CLIENT_SECRET is empty")

        return client_id, client_secret

    @staticmethod
    def get_method():
        """
        Gets login method.

        :return: str
        """

        return "github"

    @staticmethod
    def get_additional_data():
        """
        Gets additional data for login.

        :return: None
        """

        load_dotenv()
        try:
            client_id = os.environ["CLIENT_ID"]
        except KeyError:
            raise KeyError("CLIENT_ID not found in .env file") from KeyError

        if client_id == "":
            raise KeyError("CLIENT_ID is empty")

        return {"clientId": client_id}

    def authorize(self):
        """
        Authorizes GitHub login.

        :return: None
        """

        try:
            jwt_token = self.login()
            resp = make_response(redirect("/"))
            resp.set_cookie("token", jwt_token)
        except UserNotAllowed as e:
            self.logger.error(e)
            resp = make_response(redirect("/"))
            resp.status_code = 401
            resp.set_cookie("error", str(e))

        return resp

    def _get_access_token(self, request_token: str):
        """
        Gets access token from GitHub.

        :param request_token:
        :return: str
        """

        client_id, client_secret = self._get_id_and_secret()

        auth_data = {
            "code": request_token,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": "http://127.0.0.1:5000/github/callback",
        }
        resp = requests.post(
            "https://github.com/login/oauth/access_token", data=auth_data, timeout=10
        )
        token = resp.text.split("access_token=")[1]
        token = token.split("&")[0]

        return token

    @staticmethod
    def _get_user_data(access_token: str) -> dict:
        """
        Gets user data from GitHub.

        :param access_token: Access token
        :return: dict
        """
        if not access_token:
            raise ValueError("The request token has to be supplied!")
        if not isinstance(access_token, str):
            raise ValueError("The request token has to be a string!")

        user = requests.get(
            "https://api.github.com/user",
            headers={"Authorization": "token " + access_token},
            timeout=10,
        )

        return user.json()
