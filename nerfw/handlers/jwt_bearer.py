import logging
import os

import jwt
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self._logger = logging.getLogger(self.__class__.__name__)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwt_token: str) -> bool:
        """
        Verify JWT token

        :param jwt_token: JWT token
        :return: True if token is valid, False otherwise
        """

        is_token_valid: bool = False

        try:
            payload = self.decode_jwt(jwt_token)
        except HTTPException:
            payload = None

        if payload:
            is_token_valid = True
            self._logger.debug(f"Token is valid: {is_token_valid}")
        else:
            self._logger.error(f"Token is not valid: {is_token_valid}")

        return is_token_valid

    @staticmethod
    def decode_jwt(token: str):
        """
        Decode JWT token

        :param token: JWT token
        :return: Decoded token
        """

        try:
            payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=403, detail="Signature has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=403, detail="Invalid token")
        except Exception:
            raise HTTPException(status_code=403, detail="Invalid token")
