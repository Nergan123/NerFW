from nerfw.helpers.logger import LoggerBase
from nerfw.server.server import Server


class NerFW(LoggerBase):
    """
    Main class for Ner framework
    """

    def __init__(self):
        super().__init__()
        self.logger.info("Initializing NerFW")

    def run(self, script, debug=False, port=4000):
        """
        Runs a game
        :return: None
        """

        server = Server()
        self.logger.info("Launching NerFW")
        server.run(script, debug=debug, port=port)
