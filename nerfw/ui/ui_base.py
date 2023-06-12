from nerfw.ui.button import Button
from nerfw.ui.functions import Functions
from nerfw.helpers import LoggerBase
from nerfw.ui.input_text import InputText


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
        self.logger.info(f"Adding button to: {self.__class__.__name__}")
        self.buttons.append(but)

    def add_input(self, input_name: str, pos: (int, int), length: (int, int), size: int):
        """
        Adds a text field to the menu
        :param input_name: Name that will be displayed
        :param pos: Position on screen in percents
        :param length: Tuple containing min and max length of the input
        :param size: Size to display
        """

        inp = InputText(input_name, pos, length, size)
        self.logger.info(f"Adding input field to: {self.__class__.__name__}")
        self.buttons.append(inp)
