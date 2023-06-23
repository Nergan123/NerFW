from nerfw.helpers import LoggerBase


class TextField(LoggerBase):
    """
    Class containing text output field
    """

    def __init__(self, name: str, pos: (int, int), font_size: int):
        super().__init__()
        self.name = name
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.size = font_size

    def compile(self):
        """
        Returns css and html
        :return: css, html
        """

        html = f"<p id='{self.name}'> "
        html += "{{ text|safe }} </p>"
        css = f"top:{self.pos_y}%;"
        css += f"left:{self.pos_x}%;"
        css += "position: absolute;"
        css += f"font-size: {self.size}px;"

        return html, css
