from nerfw.helpers import LoggerBase


class InputText(LoggerBase):
    """
    Creates an input field in html
    """

    def __init__(self, input_name: str, pos: (int, int), length: (int, int), size: int):
        """
        Creates a field
        :param input_name: Name that will be displayed
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

    def compile(self):
        """
        Returns css and html
        :return: css, html
        """

        html = f"<input type='text' id='{self.name}' name='{self.name}' " \
               f"required minlength='{self.min}' maxlength='{self.max}' size='{self.size}'>"

        css = f"top:{self.y}%;"
        css += f"left:{self.x}%;"
        css += "position: absolute;"

        return html, css
