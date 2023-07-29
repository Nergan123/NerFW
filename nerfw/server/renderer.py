from nerfw.helpers.logger import LoggerBase
from nerfw.helpers.breaker import Breaker
from nerfw.helpers.deconstructor import Deconstructor
from nerfw.helpers.img_handler import ImageHandler


class Renderer(LoggerBase):
    """Class to render html"""

    def __init__(self):
        super().__init__()
        self.logger.debug("Created")
        self.deconstructor = Deconstructor()
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
        :return: dict
        """

        styles = {}

        back = "background-image: url(data:image/jpeg;base64,"
        back += scene["background"]
        back += "); background-repeat: no-repeat; " \
                "background-size: cover; " \
                "background-position: center; "

        styles["body_element"] = back
        try:
            char = scene["characters"][0]
            styles[char.name] = "position: absolute;"
            styles[char.name] += f"top: {char.animation.current_y}%;"
            styles[char.name] += f"left: {char.animation.current_x}%;"
            styles[char.name] += char.animation.css
        except IndexError:
            pass

        if scene["choice"] is not None:
            pass

        self.logger.debug(f"Returning css: {styles}")
        return styles

    def compile_html(self, scene: dict):
        """
        Compiles html to be returned
        :param scene: Scene dict
        :return: str
        """

        html = {}

        if len(scene["characters"]) > 0:
            char = scene["characters"][0]
            char_img = self.image_handler.convert_to_base64(char.img)
            html["show-data"] = f"<img id={char.name} src='data:image/jpeg;base64, {char_img}' />"
            html["char-name"] = f"<p><b> {char.name}: <b><p>"
            html["char-text"] = f"<p> {scene['text']} <p>"
        else:
            html["show-data"] = ""
            html["char-name"] = "<p><b> ...: <b><p>"
            html["char-text"] = f"<p> {scene['text']} <p>"

        if scene["choice"] is not None:
            html["show-data"] += scene['choice'].compile()
            html["char-name"] = ""
            html["char-text"] = ""

        html["player"] = scene["audio"]

        return html
