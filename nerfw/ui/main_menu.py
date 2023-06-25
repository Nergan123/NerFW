from nerfw.ui.functions import Functions
from nerfw.ui.ui_base import UiBase


class MainMenu(UiBase):
    """
    Class for creation and control of main menu
    """

    def __init__(self):
        super().__init__()
        self.id = "main_menu"
        self.setup()

    def setup(self):
        """
        Sets up a ui
        :return: None
        """

        self.add_button("Game", (10, 70), Functions.REDIRECT_GAME)
