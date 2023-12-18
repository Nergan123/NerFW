import unittest
from nerfw.game.animation import Animations


class TestAnimations(unittest.TestCase):
    """
    Unit test class for the Animations class in the nerfw.game.animation module.
    """

    def setUp(self):
        """
        Set up method for the test class. Initializes an instance of the Animations class.
        """
        self.animations = Animations(0, 0)

    def test_move_changes_current_position(self):
        """
        Test case to verify that the move method correctly updates the current position.
        """
        self.animations.move(10, 20, 1)
        self.assertEqual(self.animations.current_x, 10)
        self.assertEqual(self.animations.current_y, 20)

    def test_move_updates_css(self):
        """
        Test case to verify that the move method correctly updates the CSS properties.
        """
        self.animations.move(10, 20, 1)
        expected_css = {
            "position": "absolute",
            "--moveStartX": "0%",
            "--moveEndX": "10%",
            "--moveStartY": "0%",
            "--moveEndY": "20%",
            "animation": "1s ease-in-out 0s 1 slideIn",
            "top": "20%",
            "left": "10%",
        }
        self.assertEqual(self.animations.css, expected_css)

    def test_move_with_negative_values(self):
        """
        Test case to verify that the move method correctly handles negative values.
        """
        self.animations.move(-10, -20, 1)
        self.assertEqual(self.animations.current_x, -10)
        self.assertEqual(self.animations.current_y, -20)

    def test_move_with_zero_duration(self):
        """
        Test case to verify that the move method correctly handles a duration of zero.
        """
        self.animations.move(10, 20, 0)
        self.assertEqual(self.animations.current_x, 10)
        self.assertEqual(self.animations.current_y, 20)

    def test_move_with_large_values(self):
        """
        Test case to verify that the move method correctly handles large values.
        """
        self.animations.move(10000, 20000, 1)
        self.assertEqual(self.animations.current_x, 10000)
        self.assertEqual(self.animations.current_y, 20000)


if __name__ == "__main__":
    unittest.main()
