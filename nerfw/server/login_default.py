from nerfw.helpers.errors.user_not_allowed import UserNotAllowed
from nerfw.helpers.db_handler import DbHandler
from nerfw.helpers.errors.password_mismatch import PasswordsMismatch
from nerfw.helpers.errors.user_doesnt_exist import UserDoesntExist
from nerfw.helpers.login_base import LoginBaseClass
from nerfw.server.password_manager import PasswordManager


class LoginDefault(LoginBaseClass):
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

        if not self.check_user_allowed(data["Login"]):
            raise UserNotAllowed(data["Login"])

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
