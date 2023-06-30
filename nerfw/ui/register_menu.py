from nerfw.ui.functions import Functions
from nerfw.ui.ui_base import UiBase


class RegisterMenu(UiBase):
    """
    register page menu
    """

    def __init__(self):
        super().__init__()
        self.id = "register_menu"
        self.setup()

    def setup(self):
        """
        Sets up a ui
        :return: None
        """

        self.add_input("Login", Functions.INPUT_TEXT, (45, 45), (4, 20), 20)
        self.add_input("Password", Functions.INPUT_TEXT, (45, 48), (4, 20), 20)
        self.add_input("Repeat_password", Functions.INPUT_TEXT, (45, 51), (4, 20), 20)
        self.add_input("Submit", Functions.INPUT_SUBMIT, (45, 54), (4, 20), 20)
