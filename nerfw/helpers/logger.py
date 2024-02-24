import os
import logging


class LoggerBase:
    """ Class for log handling """

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    @staticmethod
    def setup_logger():
        """
        Sets up logging

        :return: None
        """

        if not os.path.isdir('logs'):
            os.makedirs('logs')

        fmt = '%(asctime)s [%(name)s]: %(levelname)s: %(message)s'

        stdout_handler = logging.StreamHandler()
        stdout_handler.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler("logs/logs.log", 'a')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(fmt))

        logging.basicConfig(
            level=logging.DEBUG,
            handlers=[
                stdout_handler,
                file_handler
            ]
        )
