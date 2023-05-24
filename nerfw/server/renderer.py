from nerfw.helpers import LoggerBase
from nerfw.helpers.breaker import Breaker
from nerfw.helpers.deconstructor import Deconstructor
from nerfw.helpers.img_handler import ImageHandler
from nerfw.ui.ui import Ui


class Renderer(LoggerBase):
    """Class to render html"""

    def __init__(self, ui: Ui):
        super().__init__()
        self.logger.debug("Created")
        self.deconstructor = Deconstructor()
        self.ui = ui
        self.image_handler = ImageHandler()

    def render(self, breaker: Breaker):
        """
        Renders a scene
        :param breaker: Breaker containing all the scene info
        :return: HTML
        """

        self.logger.debug(f"Received: {breaker}")
        scene = self.deconstructor.deconstruct(breaker)

        html = self.compile_html(scene)
        css = self.compile_css(scene)
        self.logger.info("Returning scene")

        return html, css

    def compile_css(self, scene: dict):
        """
        Compiles css to be rendered
        :param scene: Scene dict after deconstruction
        :return: str
        """

        back = "url('data:image/jpeg;base64,"
        back += scene["background"]

        self.logger.debug(f"Returning css: {back}")
        return back

    def compile_html(self, scene: dict):
        """
        Compiles html to be returned
        :param scene: Scene dict
        :return: str
        """

        if len(scene["characters"]) > 0:
            char = scene["characters"][0]
            char_img = self.image_handler.convert_to_base64(char.img)
            char_img = f"<img src='data:image/jpeg;base64, {char_img}' />"
            html = f"<p><b> {char.name}: <b><p>"
            html += f"<p> {scene['text']} <p><br>"
            html += char_img
        else:
            html = "<p><b> ...: <b><p>"
            html += f"<p> {scene['text']} <p><br>"

        return html
