from nerfw.ui.button import Button
from nerfw.ui.functions import Functions
from nerfw.helpers import LoggerBase


class UiBase(LoggerBase):
    """Main class for ui"""

    def __init__(self):
        super().__init__()
        self.buttons = []

    def add_button(self, name: str, pos: (int, int), function: Functions):
        """
        Creates a button for the ui
        :param name: Name to display
        :param pos: Position on screen
        :param function: Function to assign
        :return: None
        """

        but = Button(name, pos, function)
        self.logger.info(f"Created a button: {name}")
        self.buttons.append(but)
