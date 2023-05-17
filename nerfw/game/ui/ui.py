from nerfw.game.ui.button import Button
from nerfw.game.ui.functions import Functions
from nerfw.helpers import LoggerBase


class Ui(LoggerBase):
    """Main class for ui"""

    def __init__(self):
        super().__init__()
        self.buttons = []
        self.html = ""

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

    def compile(self):
        """
        Compiles complete html and ui
        :return: html
        """

        css_buttons = []
        html_buttons = []
        for button in self.buttons:
            html, css = button.compile()
            css_buttons.append(css)
            html_buttons.append(html)

        with open("nerfw/server/templates/head.html", "r") as template:
            html = template.read()

        html += "<style>"
        for css in css_buttons:
            html += css
        html += "</style>"

        with open("nerfw/server/templates/body.html", "r") as template:
            html += template.read()

        for but in html_buttons:
            html += but

        with open("nerfw/server/templates/tail.html", "r") as template:
            html += template.read()

        self.logger.debug(f"final html: {html}")
        with open("nerfw/server/templates/index.html", "w") as template:
            template.write(html)
