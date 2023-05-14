from nerfw.helpers import LoggerBase
from nerfw.nerfw import NerFW


if __name__ == "__main__":
    LoggerBase.setup_logger()
    app = NerFW()
    Tester = app.create_character("Tester", "test_files/test.jpg", (100, 255, 255))
    Tester.say("Test 1")
    Tester.say("Test 2")
    app.run()
