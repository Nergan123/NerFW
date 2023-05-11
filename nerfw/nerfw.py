from nerfw.helpers import LoggerBase
from nerfw.server.server import Server


class NerFW(LoggerBase):
    """
    Main class for Ner framework
    """

    def __init__(self):
        super().__init__()
        self.server = Server()

    def run(self, debug=False):
        """
        Runs a game
        :return: None
        """

        self.logger.info("Launching NerFW")
        self.server.run(debug=debug)
