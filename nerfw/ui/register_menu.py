from nerfw.ui.functions import Functions
from nerfw.ui.ui_base import UiBase


class RegisterMenu(UiBase):
    """
    register page menu
    """

    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        """
        Sets up a ui
        :return: None
        """

        self.add_text_field("Output", (45, 40), 40)
        self.add_input("Login", Functions.INPUT_TEXT, (45, 50), (4, 20), 20)
        self.add_input("Password", Functions.INPUT_TEXT, (45, 52), (4, 20), 20)
        self.add_input("Repeat_password", Functions.INPUT_TEXT, (45, 54), (4, 20), 20)
        self.add_input("Submit", Functions.INPUT_SUBMIT, (45, 56), (4, 20), 20)
