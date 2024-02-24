import os

import patreon
import requests
from dotenv import load_dotenv
from flask import make_response, redirect, request

from nerfw.helpers.errors.user_not_allowed import UserNotAllowed
from nerfw.helpers.login_base import LoginBaseClass
from nerfw.server.token_handler import TokenHandler


class LoginPatreon(LoginBaseClass):
    """
    Login to Patreon.
    """

    def __init__(self):
        super().__init__()
        self.token_handler = TokenHandler()

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

    def login(self):
        """
        Login to Patreon.

        :return: JWT token
        """

        self.logger.info("Authorizing Patreon login...")
        client_id, client_secret = self._get_id_and_secret()
        oauth_client = patreon.OAuth(client_id, client_secret)
        tokens = oauth_client.get_tokens(
            request.args.get("code"), "http://127.0.0.1:5000/patreon/callback"
        )
        access_token = tokens["access_token"]
        user_response = self.get_user_data(access_token)
        campaign = self.get_campaign_id()

        if not self.check_user_is_patron(user_response, campaign):
            raise UserNotAllowed(
                user_response["included"][0]["attributes"]["full_name"]
            )

        jwt_token = self.token_handler.create_token(
            user_response["included"][0]["attributes"]["full_name"]
        )

        return jwt_token

    @staticmethod
    def get_creator_token():
        """
        Gets creator token.

        :return: str
        """

        load_dotenv()
        try:
            creator_token = os.environ["CREATOR_TOKEN"]
        except KeyError:
            raise KeyError("CREATOR_TOKEN not found in .env file") from KeyError

        if creator_token == "":
            raise KeyError("CREATOR_TOKEN is empty")

        return creator_token

    @staticmethod
    def get_method():
        """
        Gets login method.

        :return: str
        """

        return "patreon"

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

        redirect_url = "http://127.0.0.1:5000/patreon/callback"

        return {"clientId": client_id, "redirectUrl": redirect_url}

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

    @staticmethod
    def get_user_data(access_token: str):
        """
        Gets user data.

        :param access_token: Access token
        :return:
        """

        url = (
            "https://www.patreon.com/api/oauth2/v2/identity"
            "?include=memberships.campaign&fields%5Bmember%5D=patron_status,full_name"
        )

        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(
            url,
            headers=headers,
            timeout=10,
        )

        return response.json()

    def get_campaign_id(self):
        """
        Gets current patrons.

        :return: Campaign id
        """

        creator_token = self.get_creator_token()
        headers = {"Authorization": f"Bearer {creator_token}"}
        response = requests.get(
            "https://patreon.com/api/oauth2/v2/campaigns?fields%5Bcampaign%5D=creation_name",
            headers=headers,
            timeout=10,
        )

        data = response.json()["data"]
        id_list = [campaign["id"] for campaign in data if campaign]

        return id_list[0]

    @staticmethod
    def check_user_is_patron(user_data: dict, campaign_id: str):
        """
        Checks if user is a patron.

        :param user_data: User data
        :param campaign_id: Campaign id
        :return: bool
        """

        for obj in user_data["included"]:
            try:
                if (
                    obj["relationships"]["campaign"]["data"]["id"] == campaign_id
                    and obj["attributes"]["patron_status"] == "active_patron"
                ):
                    return True
            except KeyError:
                pass

        return False
