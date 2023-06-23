from nerfw.helpers import LoggerBase
from nerfw.helpers.db_handler import DbHandler
from nerfw.helpers.errors.password_mismatch import PasswordsMismatch
from nerfw.helpers.errors.user_doesnt_exist import UserDoesntExist


class LoginHandler(LoggerBase):
    """
    Handles login process
    """

    def __init__(self):
        super().__init__()
        self.db = DbHandler()

    def login(self, data: dict):
        """
        Checks user data
        :param data: Login credentials
        :return: bool
        """

        sql = "SELECT password FROM credentials WHERE login = ?"
        result = self.db.execute(sql, data["Login"])
        self.logger.debug(f"Found results: {result}")
        if len(result) != 1:
            raise UserDoesntExist(data["Login"])
        return result[0]

    def register(self, data: dict):
        """
        Registers new user
        :param data: Login credentials
        :return: bool
        """

        self.logger.debug(f"Received: {data}")
        sql = "INSERT INTO credentials(login, password) VALUES(?, ?)"
        if data["Password"] != data["Repeat_password"]:
            raise PasswordsMismatch()
        values = [data["Login"][0], data["Password"][0]]
        self.db.execute(sql, values)
