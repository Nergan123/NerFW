from nerfw.helpers import LoggerBase
from nerfw.nerfw import NerFW


if __name__ == "__main__":
    LoggerBase.setup_logger()
    app = NerFW()
    app.run()
