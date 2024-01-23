from nerfw.helpers.errors.unsupported_login_method import UnsupportedLoginMethodError
from nerfw.helpers.logger import LoggerBase
from nerfw.server.server import Server


class NerFW(LoggerBase):
    """
    Main class for Ner framework
    """

    def __init__(self):
        super().__init__()
        self.logger.info("Initializing NerFW")
        self.login_method = "default"
        self.allowed_users = []

    def run(self, script, debug=False):
        """
        Runs a game
        :param script: Script to run
        :param debug: Debug mode
        :return: None
        """

        server = Server(self.login_method)
        server.login_handler.set_list_of_allowed_users(self.allowed_users)
        self.logger.info("Launching NerFW")
        server.run(script, debug=debug)

    def set_login_method(self, method: str):
        """
        Sets login method
        :param method: Login method. Can be "Default", "GitHub"
        :return: None
        """

        if method.lower() not in ["default", "github"]:
            raise UnsupportedLoginMethodError(method)

        self.logger.info(f"Setting login method to {method}")
        self.login_method = method

    def set_allowed_users(self, users: str):
        """
        Sets list of allowed users
        :param users: path to file with list of users
        :return: None
        """

        with open(users) as f:
            users = f.readlines()
        self.allowed_users = users
