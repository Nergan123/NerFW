from nerfw.helpers import LoggerBase


class Renderer(LoggerBase):
    """Class to render html"""

    def __init__(self):
        super().__init__()
        self.logger.debug("Created")

    def render(self, json_scene: dict):
        """
        Renders a scene
        :param json_scene: A dict containing all the info
        :return: HTML
        """

        self.logger.debug(f"Received: {json_scene}")

        html = f"<p><b> {json_scene['line']['name']}: <b><p>"
        html += f"<p> {json_scene['line']['text']} <p><br>"
        self.logger.info(f"Returning: {html}")

        return html
