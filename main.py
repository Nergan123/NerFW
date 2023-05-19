from nerfw import Game, Functions, NerFW
from nerfw.helpers import LoggerBase


def script(last_line):
    """
    Game script to be run
    :param last_line: Required to run
    :return: None
    """

    app = Game(last_line)

    tester = app.create_character("Tester", "test_files/test.jpg", (100, 255, 255))
    coder = app.create_character("Coder", "test_files/test.jpg", (255, 100, 100))

    tester.say("Test 1")
    tester.say("Test 2")

    coder.say("What are you testing?")


if __name__ == "__main__":
    LoggerBase.setup_logger()
    ner = NerFW()
    ner.ui.add_button("next", (10, 70), Functions.FORWARD)
    ner.ui.add_button("next2", (90, 70), Functions.FORWARD)
    ner.ui.compile()

    ner.run(script)
