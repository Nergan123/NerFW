from nerfw import Game
from nerfw.game.ui.functions import Functions
from nerfw.helpers import LoggerBase
from nerfw.nerfw import NerFW


def script(last_line):
    """
    Game script to be run
    :return: None
    """

    app = Game(last_line)
    app.ui.add_button("next", (10, 10), Functions.FORWARD)
    app.ui.add_button("next2", (90, 70), Functions.FORWARD)
    app.ui.compile()

    tester = app.create_character("Tester", "test_files/test.jpg", (100, 255, 255))
    coder = app.create_character("Coder", "test_files/test.jpg", (255, 100, 100))

    tester.say("Test 1")
    tester.say("Test 2")

    coder.say("What are you testing?")


if __name__ == "__main__":
    LoggerBase.setup_logger()
    ner = NerFW()
    ner.run(script)
