import enum

from nerfw.helpers import LoggerBase
# pylint: disable=too-many-arguments


class InputText(LoggerBase):
    """
    Creates an input field in html
    """

    def __init__(
        self,
        input_name: str,
        input_type: enum,
        pos: (int, int),
        length: (int, int),
        size: int,
    ):
        """
        Creates a field
        :param input_name: Name that will be displayed
        :param input_type: Sets type for input field
        :param pos: Position on screen in percents
        :param length: Tuple containing min and max length of the input
        :param size: Size to display
        """

        super().__init__()
        self.name = input_name
        self.x = pos[0]
        self.y = pos[1]
        self.min = length[0]
        self.max = length[1]
        self.size = size
        self.input_type = input_type

    def compile(self):
        """
        Returns css and html
        :return: css, html
        """

        if self.input_type.value == "text":
            html = (
                f"<input type='text' id='{self.name}' name='{self.name}' "
                f"required minlength='{self.min}' maxlength='{self.max}' "
                f"size='{self.size}' value='{self.name}'>"
            )

            css = f"top:{self.y}%;"
            css += f"left:{self.x}%;"
            css += "position: absolute;"
        else:
            html = (
                f"<input type='submit' id='{self.name}' name='{self.name}' "
                f"size='{self.size}' value='{self.name}'>"
            )

            css = f"top:{self.y}%;"
            css += f"left:{self.x}%;"
            css += "position: absolute;"

        return html, css
