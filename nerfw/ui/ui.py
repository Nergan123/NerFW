from nerfw.helpers import LoggerBase
from nerfw.ui.main_menu import MainMenu


class Ui(LoggerBase):
    """
    Contains all UIs
    """

    def __init__(self):
        super().__init__()
        self.main_menu = MainMenu()
