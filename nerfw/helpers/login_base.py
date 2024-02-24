from nerfw.helpers.logger import LoggerBase


class LoginBaseClass(LoggerBase):
    """
    Base class for login methods.
    """

    def __init__(self):
        super().__init__()
        self.allowed_users = []

    def check_user_allowed(self, login: str):
        """
        Checks if user is allowed

        :param login: User login
        :return: bool
        """

        return login in self.allowed_users if self.allowed_users else True

    @staticmethod
    def get_method():
        """
        Returns method name.

        :return: str
        """

        raise NotImplementedError

    @staticmethod
    def get_additional_data():
        """
        Gets additional data for login

        :return: None
        """

        return None

    def authorize(self):
        """
        Checks if user is authorized

        :return: None
        """

        return None

    def set_list_of_allowed_users(self, users: list):
        """
        Sets list of allowed users

        :param users: List of users
        :return: None
        """

        self.allowed_users = users
