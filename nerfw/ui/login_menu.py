from nerfw.ui.ui_base import UiBase


class LoginMenu(UiBase):
    """
    Class for creation and control of main menu
    """

    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        """
        Sets up a ui
        :return: None
        """

        self.add_input("Login", (50, 50), (4, 20), 20)
