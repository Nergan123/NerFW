from nerfw.game.ui.functions import Functions
from nerfw.helpers import LoggerBase
from nerfw.nerfw import NerFW


if __name__ == "__main__":
    LoggerBase.setup_logger()
    app = NerFW()
    app.ui.add_button("next", (10, 10), Functions.FORWARD)
    app.ui.add_button("next2", (10, 50), Functions.FORWARD)
    app.ui.compile()
    Tester = app.create_character("Tester", "test_files/test.jpg", (100, 255, 255))
    Coder = app.create_character("Coder", "test_files/test.jpg", (255, 100, 100))

    Tester.say("Test 1")
    Tester.say("Test 2")

    Coder.say("What are you testing?")

    app.run()
