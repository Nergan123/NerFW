import unittest
from unittest.mock import MagicMock
from nerfw.game.choice import Choice
from nerfw.helpers.recorder import Recorder


class ChoiceTest(unittest.TestCase):
    """
    This class contains unit tests for the Choice class in the nerfw.game.choice module.
    """

    def setUp(self):
        """
        This method sets up the necessary objects for the tests.
        It is called before each test method is executed.
        """
        self.recorder = MagicMock(spec=Recorder)
        self.recorder.check.return_value = [True, False, False]
        self.recorder.scene = MagicMock()
        self.choice = Choice(
            self.recorder,
            ["choice1", "choice2", "choice3"],
            {"choices": {"1": "choice1"}},
            "1",
        )

    def test_choice_to_dict(self):
        """
        This test checks if the choice object is correctly converted to a dictionary.
        """
        result = self.choice.to_dict()
        self.assertEqual(len(result["options"]), 3)
        self.assertEqual(result["options"][0], {"id": "1", "text": "choice1"})

    def test_setup_with_existing_answers(self):
        """
        This test checks if the setup method correctly sets
        the answers attribute when there are existing answers.
        """
        self.choice.setup()
        self.assertEqual(self.choice.answers, [True, False, False])

    def test_setup_without_existing_answers(self):
        """
        This test checks if the setup method correctly sets
        the answers attribute when there are no existing answers.
        """
        self.choice.cookies = {"choices": {}}
        self.choice.setup()
        self.assertEqual(self.choice.answers, [])

    def test_make_choice(self):
        """
        This test checks if the make method correctly returns the answers.
        """
        result = self.choice.make()
        self.assertEqual(result, [True, False, False])


if __name__ == "__main__":
    unittest.main()
