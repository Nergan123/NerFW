from nerfw.helpers.logger import LoggerBase


class ErrorHandler(LoggerBase):
    """
    Class for handling errors
    """

    def __init__(self):
        super().__init__()
        self.logger.debug("Activated")

    def display(self, error: str):
        """
        Creates a popup message
        :param error: Error text to display
        :return: html
        """

        self.logger.debug(f"Creating popup for: {error}")
        error = f'"{error}"'
        html = "<div id='error'>"
        html += "<script type='text/javascript'>"
        html += f"alert({error})"
        html += "</script>"
        html += "</div>"

        return html
