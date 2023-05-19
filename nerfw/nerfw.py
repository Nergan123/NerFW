from nerfw.helpers import LoggerBase
from nerfw.server.server import Server
from nerfw.ui.ui import Ui


class NerFW(LoggerBase):
    """
    Main class for Ner framework
    """

    def __init__(self):
        super().__init__()
        self.logger.info("Initializing NerFW")
        self.ui = Ui()

    def run(self, script, debug=False):
        """
        Runs a game
        :return: None
        """

        server = Server()
        self.logger.info("Launching NerFW")
        server.run(script, debug=debug)
