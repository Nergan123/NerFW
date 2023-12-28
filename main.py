from nerfw import Game, NerFW
from nerfw import LoggerBase


def script(last_line):
    """
    Game script to be run
    :param last_line: Required to run
    :return: None
    """

    app = Game(last_line)
    app.set_background("test_files/back.jpg")

    tester = app.create_character(
        "Tester", "test_files/char1.png", (100, 255, 255), (30, 10)
    )
    coder = app.create_character(
        "Coder", "test_files/char1.jpeg", (255, 100, 100), (70, 10)
    )

    tester.show()
    app.play_audio("test_files/test.mp3")
    tester.say("Test 1")
    tester.animation.move(20, 10, 3)
    tester.say("Test 2")
    app.set_background("test_files/back.jpg")
    tester.hide()

    coder.say("What are you testing?")
    app.play_audio("test_files/amaranthe.mp3")
    answers = app.choice(["something", "nothing"])
    if answers[0]:
        tester.show()
        tester.say("Something")
        val = 1
    else:
        tester.show()
        tester.say("Nothing")
        val = 2

    tester.hide()
    coder.say("Got it")
    if val == 1:
        coder.say("1")
    else:
        coder.say("2")
    inner_func(tester, coder)
    tester.say("Lets test string input")
    coder.say("Ok")
    answer = app.string_input("test")
    coder.say(f"You wrote: {answer}")


def inner_func(tester, coder):
    """Just inner function"""
    coder.say("Now you are testing new function?")
    tester.show()
    tester.animation.move(40, 10, 0.5)
    tester.say("And strange values as well")
    tester.say("Lets see if I can stop moving")
    tester.say("Now")
    tester.animation.move(40, 20, 0.5)
    tester.say("Now I move again")


if __name__ == "__main__":
    LoggerBase.setup_logger()
    ner = NerFW()

    ner.run(script)
