import unittest
from unittest.mock import MagicMock
from nerfw.game.scene import Scene
from nerfw.helpers.breaker import Breaker


class BreakerTests(unittest.TestCase):
    """
    Unit test class for the Breaker class in the nerfw.helpers.breaker module.
    """

    def setUp(self):
        """
        Set up method for the test class. Initializes an instance of the Breaker class.
        """
        self.scene_mock = MagicMock(spec=Scene)
        self.breaker = Breaker("Test line", self.scene_mock)

    def test_breaker_initialization(self):
        """
        Test case to verify that the Breaker class is correctly initialized.
        """
        self.assertEqual(self.breaker.line, "Test line")
        self.assertEqual(self.breaker.scene, self.scene_mock)

    def test_breaker_exception_message(self):
        """
        Test case to verify that the Breaker class correctly sets the exception message.
        """
        try:
            raise self.breaker
        except Breaker as e:
            self.assertEqual(str(e), "Test line")


if __name__ == "__main__":
    unittest.main()
