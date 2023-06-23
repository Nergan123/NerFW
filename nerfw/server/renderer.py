from nerfw.helpers.logger import LoggerBase
from nerfw.helpers.breaker import Breaker
from nerfw.helpers.deconstructor import Deconstructor
from nerfw.helpers.img_handler import ImageHandler
from nerfw.ui.menus import Menus
from nerfw.ui.ui import Ui
from nerfw.ui.ui_base import UiBase


class Renderer(LoggerBase):
    """Class to render html"""

    def __init__(self, ui: Ui):
        super().__init__()
        self.logger.debug("Created")
        self.deconstructor = Deconstructor()
        self.ui = ui
        self.image_handler = ImageHandler()

    @staticmethod
    def render_menu(ui: UiBase):
        """
        Returns html for main menu
        :return: HTML
        """

        css = ""

        for button in ui.buttons:
            _, css_button = button.compile()
            css += f"#{button.name} "
            css += "{"
            css += css_button
            css += "}"

        for input_field in ui.inputs:
            _, css_inp = input_field.compile()
            css += f"#{input_field.name} "
            css += "{"
            css += css_inp
            css += "}"

        for text_field in ui.text_fields:
            _, css_field = text_field.compile()
            css += f"#{text_field.name} "
            css += "{"
            css += css_field
            css += "}"

        html = ""
        for button in ui.buttons:
            html_button, _ = button.compile()
            html += html_button

        html += "<form method='POST'>"

        for input_field in ui.inputs:
            html_inp, _ = input_field.compile()
            html += html_inp

        for text_field in ui.text_fields:
            html_field, _ = text_field.compile()
            html += html_field

        html += "</form>"

        return html, css

    def render(self, breaker: Breaker, menu: Menus):
        """
        Renders a scene
        :param breaker: Breaker containing all the scene info
        :param menu: A UI class to render
        :return: HTML
        """

        self.logger.debug(f"Received: {breaker}")
        scene = self.deconstructor.deconstruct(breaker)

        html = self.compile_html(scene, menu)
        css = self.compile_css(scene, menu)
        self.logger.info("Returning scene")

        return html, css

    def compile_css(self, scene: dict, menu: Menus):
        """
        Compiles css to be rendered
        :param scene: Scene dict after deconstruction
        :param menu: A UI class to render
        :return: dict
        """

        styles = {}

        back = "background-image: url(data:image/jpeg;base64,"
        back += scene["background"]
        back += "); background-repeat: no-repeat; background-size: cover;"

        styles["body_element"] = back

        for button in self.ui.__getattribute__(menu.value).buttons:
            _, styles[button.name] = button.compile()

        self.logger.debug(f"Returning css: {styles}")
        return styles

    def compile_html(self, scene: dict, menu: Menus):
        """
        Compiles html to be returned
        :param scene: Scene dict
        :param menu: A UI class to render
        :return: str
        """

        html = "<p>"
        for button in self.ui.__getattribute__(menu.value).buttons:
            html_button, _ = button.compile()
            html += html_button
        html += "</p>"

        if len(scene["characters"]) > 0:
            char = scene["characters"][0]
            char_img = self.image_handler.convert_to_base64(char.img)
            char_img = f"<img src='data:image/jpeg;base64, {char_img}' />"
            html += f"<p><b> {char.name}: <b><p>"
            html += f"<p> {scene['text']} <p><br>"
            html += char_img
        else:
            html += "<p><b> ...: <b><p>"
            html += f"<p> {scene['text']} <p><br>"

        return html
