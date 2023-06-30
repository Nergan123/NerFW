from nerfw.helpers.logger import LoggerBase
from nerfw.ui.dialogue_menu import DialogueWindow
from nerfw.ui.login_menu import LoginMenu
from nerfw.ui.main_menu import MainMenu
from nerfw.ui.register_menu import RegisterMenu


class Ui(LoggerBase):
    """
    Contains all UIs
    """

    def __init__(self):
        super().__init__()
        self.main_menu = MainMenu()
        self.dialogue_window = DialogueWindow()
        self.login_menu = LoginMenu()
        self.register_menu = RegisterMenu()
