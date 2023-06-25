from nerfw.ui.functions import Functions
from nerfw.ui.ui_base import UiBase


class LoginMenu(UiBase):
    """
    Class for creation and control of main menu
    """

    def __init__(self):
        super().__init__()
        self.id = "login_menu"
        self.setup()

    def setup(self):
        """
        Sets up a ui
        :return: None
        """

        self.add_input("Login", Functions.INPUT_TEXT, (40, 40), (4, 20), 20)
        self.add_input("Password", Functions.INPUT_TEXT, (40, 43), (4, 20), 20)
        self.add_input("Submit", Functions.INPUT_SUBMIT, (40, 46), (4, 20), 20)
