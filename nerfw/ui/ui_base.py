import enum

from nerfw.ui.button import Button
from nerfw.ui.functions import Functions
from nerfw.helpers.logger import LoggerBase
from nerfw.ui.input_text import InputText
from nerfw.ui.text_field import TextField


# pylint: disable=too-many-arguments


class UiBase(LoggerBase):
    """Main class for ui"""

    def __init__(self):
        super().__init__()
        self.buttons = []
        self.inputs = []
        self.text_fields = []

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

    def add_input(
        self,
        input_name: str,
        input_type: enum,
        pos: (int, int),
        length: (int, int),
        size: int,
    ):
        """
        Adds a text field to the menu
        :param input_name: Name that will be displayed
        :param input_type: Sets type for input field
        :param pos: Position on screen in percents
        :param length: Tuple containing min and max length of the input
        :param size: Size to display
        """

        inp = InputText(input_name, input_type, pos, length, size)
        self.logger.info(f"Adding input field to: {self.__class__.__name__}")
        self.inputs.append(inp)

    def add_text_field(self, name: str, pos: (int, int), font_size: int):
        """
        Adds a text field for a menu
        :param name:
        :param pos:
        :param font_size:
        :return:
        """

        field = TextField(name, pos, font_size)
        self.logger.info(f"Adding a text field to: {self.__class__.__name__}")
        self.text_fields.append(field)
