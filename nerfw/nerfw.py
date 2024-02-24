import typing

from nerfw.helpers.errors.unsupported_login_method import UnsupportedLoginMethodError
from nerfw.helpers.img_handler import ImageHandler
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
        self.image_handler = ImageHandler()
        self.name = "NerFW"
        self.background = {"type": "background", "data": "#282a36"}

    def run(self, script, debug=False):
        """
        Runs a game

        :param script: Script to run
        :param debug: Debug mode
        :return: None
        """

        server = Server(self.login_method, self.name)
        server.set_background(self.background)
        server.login_handler.set_list_of_allowed_users(self.allowed_users)
        self.logger.info("Launching NerFW")
        server.run(script, debug=debug)

    def set_login_method(self, method: str):
        """
        Sets login method

        :param method: Login method. Can be "Default", "GitHub"
        :return: None
        """

        if method.lower() not in ["default", "github", "patreon"]:
            raise UnsupportedLoginMethodError(method)

        self.logger.info(f"Setting login method to {method}")
        self.login_method = method

    def set_allowed_users(self, users: typing.Union[str, list]):
        """
        Sets list of allowed users

        :param users: path to file with list of users. Or list of users
        :return: None
        """

        if isinstance(users, list):
            self.allowed_users = users
            return

        with open(users) as f:
            users = f.readlines()
        self.allowed_users = users

    def set_name(self, name: str):
        """
        Sets name of the game

        :param name: Name of the game
        :return: None
        """

        self.logger.info(f"Setting name of the game to {name}")
        self.name = name

    def set_background(self, background: str):
        """
        Sets background

        :param background: Path to background
        :return: None
        """

        self.logger.info(f"Setting background to {background}")
        img = self.image_handler.convert_to_base64(background)

        self.background = {
            "type": "backgroundImage",
            "data": f"url(data:image/jpeg;base64,{img})",
        }
