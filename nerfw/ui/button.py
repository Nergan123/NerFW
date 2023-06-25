from nerfw.helpers.logger import LoggerBase
from nerfw.helpers.errors.function_not_found import FunctionNotFound
from nerfw.helpers.errors.wrong_naming import WrongNamingFormatError
from nerfw.ui.functions import Functions


class Button(LoggerBase):
    """Class for a button"""

    def __init__(self, name: str, pos: (int, int), function: Functions):
        super().__init__()
        self.name = name
        self.x = pos[0]
        self.y = pos[1]
        self.function = function
        self._check()

    def compile(self):
        """
        Returns a compiled HTML code
        :return: HTML
        """

        html = f"<button id='{self.name}' onclick="
        html += f'"{self.function.value}">{self.name}</button>'

        css = f"top:{self.y}%;"
        css += f"left:{self.x}%;"
        css += "position: absolute;"

        return html, css

    def _check(self):
        """
        Checks if everything is correct
        :return: None
        """

        if " " in self.name:
            raise WrongNamingFormatError(self.name)

        if self.function not in Functions:
            raise FunctionNotFound(self.function)
