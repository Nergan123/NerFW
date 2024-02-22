import unittest
from nerfw.helpers.input_handler import InputHandler


class InputHandlerTests(unittest.TestCase):
    """
    Unit test class for the InputHandler class in the nerfw.helpers.input_handler module.
    """

    def setUp(self):
        """
        Set up method for the test class. Initializes an instance of the InputHandler class.
        """
        self.input_handler = InputHandler("current_line", "prev_line")

    def test_input_handler_initialization(self):
        """
        Test case to verify that the InputHandler class is correctly initialized.
        """
        self.assertEqual(
            self.input_handler.cookie["lines"]["current"]["line"], "current_line"
        )
        self.assertEqual(
            self.input_handler.cookie["lines"]["previous"]["line"], "prev_line"
        )

    def test_input_handler_set_choices(self):
        """
        Test case to verify that the set_choices method correctly sets the choices in the cookie.
        """
        choices = {"choice1": "option1", "choice2": "option2"}
        self.input_handler.set_choices(choices)
        self.assertEqual(
            self.input_handler.cookie["lines"]["current"]["choices"], choices
        )

    def test_input_handler_get_current_line(self):
        """
        Test case to verify that the get_current_line
        method correctly returns the current line from the cookie.
        """
        output = self.input_handler.get_current_line()
        self.assertIn("current_line", output)

    def test_input_handler_get_prev_line(self):
        """
        Test case to verify that the get_prev_line
        method correctly returns the previous line from the cookie.
        """
        output = self.input_handler.get_prev_line()
        self.assertIn("prev_line", output)

    def test_input_handler_set_line(self):
        """
        Test case to verify that the set_line method correctly sets
        the current line in the cookie and moves the current line to the previous line.
        """
        self.input_handler.set_line("new_line")
        self.assertEqual(
            self.input_handler.cookie["lines"]["current"]["line"], "new_line"
        )
        self.assertEqual(
            self.input_handler.cookie["lines"]["previous"]["line"], "current_line"
        )

    def test_input_handler_reset(self):
        """
        Test case to verify that the reset method correctly resets the lines in the cookie.
        """
        self.input_handler.reset()
        self.assertEqual(self.input_handler.cookie["lines"]["current"]["line"], "")
        self.assertEqual(self.input_handler.cookie["lines"]["previous"]["line"], "")


if __name__ == "__main__":
    unittest.main()
