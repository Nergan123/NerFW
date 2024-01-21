from nerfw.helpers.logger import LoggerBase
from nerfw.helpers.db_handler import DbHandler
from nerfw.helpers.errors.password_mismatch import PasswordsMismatch
from nerfw.helpers.errors.user_doesnt_exist import UserDoesntExist
from nerfw.server.password_manager import PasswordManager


class LoginHandler(LoggerBase):
    """
    Handles login process
    """

    def __init__(self):
        super().__init__()
        self.db = DbHandler()
        self.pwd_manager = PasswordManager(self.db)

    def login(self, data: dict):
        """
        Checks user data
        :param data: Login credentials
        :return: dict
        """

        sql = "SELECT password, salt FROM credentials WHERE login = ?"
        result = self.db.execute(sql, [data["Login"]])
        self.logger.debug(f"Found results: {result}")
        if len(result) != 1:
            raise UserDoesntExist(data["Login"])

        hashed, _ = self.pwd_manager.encrypt(data["Password"], result[0][1])
        if hashed != result[0][0]:
            raise PasswordsMismatch()

        return result[0]

    def register(self, data: dict):
        """
        Registers new user
        :param data: Login credentials
        :return: bool
        """

        self.logger.debug(f"Received: {data}")
        if data["Password"] != data["Repeat_password"]:
            raise PasswordsMismatch()
        self.pwd_manager.register(data)

    @staticmethod
    def get_method():
        """
        Gets login method
        :return: str
        """

        return "default"

    @staticmethod
    def get_additional_data():
        """
        Gets additional data for login
        :return: None
        """

        return None
