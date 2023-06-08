from nerfw import Game, NerFW
from nerfw.helpers import LoggerBase


def script(last_line):
    """
    Game script to be run
    :param last_line: Required to run
    :return: None
    """

    app = Game(last_line)
    app.set_background("test_files/char2.jpg")

    tester = app.create_character("Tester", "test_files/test.jpg", (100, 255, 255))
    coder = app.create_character("Coder", "test_files/test.jpg", (255, 100, 100))

    tester.show()
    tester.say("Test 1")
    tester.say("Test 2")
    tester.hide()

    coder.say("What are you testing?")


if __name__ == "__main__":
    LoggerBase.setup_logger()
    ner = NerFW()

    ner.run(script)
