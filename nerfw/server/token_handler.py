import datetime
import os
import secrets

import jwt

from nerfw.helpers.logger import LoggerBase


class TokenHandler(LoggerBase):
    """
    Class for handling login token
    """

    def __init__(self):
        super().__init__()
        if not os.path.exists("data"):
            self.logger.info("Creating a data folder")
            os.mkdir("data")

        if os.path.exists("data/key.ner"):
            self.key = self.get_key()
        else:
            self.generate_key()
            self.key = self.get_key()

    def get_key(self):
        """
        Gets a key from file

        :return: key
        """

        with open("data/key.ner", "r") as file:
            key = file.read()

        self.logger.info("Received a key")
        return key

    def generate_key(self):
        """
        Generates a secret key

        :return: None
        """

        key = secrets.token_hex()
        with open("data/key.ner", "w") as file:
            file.write(key)
        self.logger.info("Generated a key at data/key.ner")

    def create_token(self, user_name: str):
        """
        Creates a session token for user

        :param user_name: Name of user
        :return: token
        """

        payload = {"login": user_name, "created": str(datetime.datetime.now())}

        token = jwt.encode(payload=payload, key=self.key, algorithm='HS256')

        return token

    def verify_token(self, token: str):
        """
        Verifies a jwt

        :param token: Lwt str token
        :return: bool or dict
        """

        if token is None:
            return False

        try:
            decoded = jwt.decode(token, key=self.key, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            self.logger.debug("Expired signature")
            return False
        return decoded

    def unlock_token(self, token: str):
        """
        Decodes token and return json obj

        :param token: JWS token
        :return: dict
        """

        decoded = jwt.decode(token, key=self.key, algorithms='HS256')

        return decoded
