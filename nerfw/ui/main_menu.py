from nerfw.ui.functions import Functions
from nerfw.ui.ui_base import UiBase


class MainMenu(UiBase):
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

        self.add_button("next", (10, 70), Functions.FORWARD)
        self.add_button("back", (90, 70), Functions.BACKWARD)
