import logging
import os
from datetime import timedelta, datetime, timezone
from enum import Enum
from typing import Tuple, Optional

import bcrypt
import jwt

from nerfw.handlers.db import DbHandler
from nerfw.models import UserModel
from nerfw.schemas.login_request import LoginRequest
from nerfw.schemas.user import User


class LoginResults(Enum):
    """Login results."""

    SUCCESS = "success"
    USER_NOT_FOUND = "user_not_found"
    INCORRECT_PASSWORD = "incorrect_password"


class LoginHandler:
    """Handles login requests."""

    def __init__(self):
        self.db = DbHandler()
        self._logger = logging.getLogger(self.__class__.__name__)

    async def login(self, request: LoginRequest) -> Tuple[LoginResults, Optional[User]]:
        """
        Handles login requests.

        :param request: Login request
        :return: Login result and user object
        """

        async with self.db as db:
            db_user = (
                db.query(UserModel)
                .filter(UserModel.username == request.username)
                .first()
            )

        if db_user is None:
            self._logger.debug("User not found")
            return LoginResults.USER_NOT_FOUND, None

        self._logger.debug(f"User: {db_user.username}")
        hashed_password = db_user.password.encode("utf-8")
        if not self._verify_password(request.password, hashed_password):
            self._logger.debug("Incorrect password")
            return LoginResults.INCORRECT_PASSWORD, None

        self._logger.debug("Login successful")
        return LoginResults.SUCCESS, User(
            username=db_user.username, role=db_user.role, id=db_user.id
        )

    @staticmethod
    async def sign_jwt(user: User) -> str:
        """
        Signs a JWT.

        :param user: User
        :return: JWT
        """

        expire = timedelta(days=1)
        to_encode = {
            "user": user.model_dump(),
            "exp": datetime.now(tz=timezone.utc) + expire,
        }
        token = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm="HS256")

        return token

    def _hash_password(self, password: str) -> bytes:
        """
        Hashes a password.

        :param password: Password
        :return: Hashed password
        """

        self._logger.debug("Hashing password")
        password = password.encode("utf-8")
        output = bcrypt.hashpw(password, bcrypt.gensalt(12))

        return output

    def _verify_password(self, password: str, hashed_password: bytes) -> bool:
        """
        Verifies a password.

        :param password: Password
        :param hashed_password: Hashed password
        :return: True if the password is correct, False otherwise
        """

        self._logger.debug("Verifying password")
        password = password.encode("utf-8")

        result = bcrypt.checkpw(password, hashed_password)

        return result
