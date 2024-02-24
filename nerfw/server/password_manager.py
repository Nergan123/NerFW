import hashlib
import random
import sqlite3
import string

from nerfw.helpers.errors.user_already_registered import UserAlreadyRegistered

from nerfw.helpers.db_handler import DbHandler

from nerfw.helpers.logger import LoggerBase


class PasswordManager(LoggerBase):
    """
    Class to manage passwords in db
    """

    def __init__(self, db: DbHandler):
        super().__init__()
        self.db = db

    def register(self, data: dict):
        """
        Registers a password in db

        :param data: Data from web
        :return: None
        """

        pwd = data["Password"]
        self.logger.debug(f"Hashing password for {data['Login']}")
        hashed, salt = self.encrypt(pwd)
        sql = "INSERT INTO credentials(login, salt, password) VALUES(?, ?, ?)"
        vals = [data["Login"], salt, hashed]
        try:
            self.db.execute(sql, vals)
        except sqlite3.IntegrityError as e:
            raise UserAlreadyRegistered(data["Login"]) from e

    @staticmethod
    def encrypt(password: str, salt=None):
        """
        Encrypts a password

        :param password: Provided password
        :param salt: Salt to be used
        :return: Hashed password
        """

        if salt is None:
            salt = "".join(random.choices(string.ascii_letters + string.digits, k=25))

        pwd = f"{password}{salt}"
        hashed = hashlib.sha256(pwd.encode()).hexdigest()

        return hashed, salt
