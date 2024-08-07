from nerfw import Game, NerFW
from nerfw import LoggerBase


def script(*args, **kwargs):
    """
    Game script to be run
    :return: None
    """

    app = Game(*args, **kwargs)
    app.set_background("tests/integration_testing/test_files/back.jpg")

    tester = app.create_character(
        "Tester",
        "tests/integration_testing/test_files/char1.png",
        (100, 255, 255),
        (30, 10),
    )
    coder = app.create_character(
        "Coder",
        "tests/integration_testing/test_files/char1.jpeg",
        (255, 100, 100),
        (70, 10),
    )

    tester.show()
    app.play_audio("tests/integration_testing/test_files/test.mp3")
    tester.say("Test 1")
    tester.animation.move(20, 10, 3)
    tester.scale(height=5000, width=500)
    tester.say("Test 2")
    tester.say("Test 3")
    tester.say("Test 4")
    app.unlock_scene("tests/integration_testing/test_files/back.jpg", "back", "test")
    app.unlock_scene("tests/integration_testing/test_files/char1.jpeg", "coder", "test")
    app.unlock_scene("tests/integration_testing/test_files/char1.jpeg", "coder1New", "coders")
    app.unlock_scene("tests/integration_testing/test_files/char1.jpeg", "coder2New", "coders")
    app.unlock_scene("tests/integration_testing/test_files/char1.jpeg", "coder3New", "coders")
    app.set_background("tests/integration_testing/test_files/back.jpg")
    tester.hide()

    coder.say("What are you testing?")
    app.stop_audio("tests/integration_testing/test_files/test.mp3")
    app.play_audio("tests/integration_testing/test_files/test2.mp3", repeat=True)
    answers = app.choice(["something", "nothing"])
    if answers[0]:
        tester.show()
        tester.say("Something")
        val = 1
    else:
        tester.show()
        tester.say("Nothing")
        val = 2

    app.unlock_scene("tests/integration_testing/test_files/char1.png", "tester", "test")
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

    tester.say("Lets test a for loop")
    for i in range(5):
        tester.say(f"Loop {i}")

    coder.say("Well seems working")


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
    ner.set_name("Test game")
    ner.set_background("tests/integration_testing/test_files/back.jpg")

    ner.run(script)
