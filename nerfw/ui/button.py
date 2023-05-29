from nerfw.ui.functions import Functions
from nerfw.helpers import LoggerBase


class Button(LoggerBase):
    """Class for a button"""

    def __init__(self, name: str, pos: (int, int), function: Functions):
        super().__init__()
        self.name = name
        self.x = pos[0]
        self.y = pos[1]
        self.function = function.value

    def compile(self):
        """
        Returns a compiled HTML code
        :return: HTML
        """

        html = f"<button id='{self.name}' onclick="
        html += f"'{self.function}'>{self.name}</button>"

        css = f"top:{self.y}%;"
        css += f"left:{self.x}%;"
        css += "width:100px;" \
               "height:40px;" \
               "position: absolute;"

        return html, css
