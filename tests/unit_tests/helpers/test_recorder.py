import unittest
from unittest.mock import MagicMock
from nerfw.helpers.recorder import Recorder
from nerfw.game.scene import Scene
from nerfw.helpers.breaker import Breaker


class RecorderTests(unittest.TestCase):
    """
    Unit test class for the Recorder class in the nerfw.helpers.recorder module.
    """

    def setUp(self):
        """
        Set up method for the test class. Initializes an instance of the Recorder class.
        """
        self.scene_mock = MagicMock(spec=Scene)
        self.recorder = Recorder('{"line": "line1", "back": false}', self.scene_mock)

    def test_recorder_initialization(self):
        """
        Test case to verify that the Recorder class is correctly initialized.
        """
        self.assertEqual(self.recorder.previous["line"], "line1")
        self.assertEqual(self.recorder.previous["back"], False)
        self.assertEqual(self.recorder.scene, self.scene_mock)

    def test_recorder_check_report_no_back(self):
        """
        Test case to verify that the check method correctly raises a Breaker
        exception when report is True and the input line is the same as the previous line.
        """
        self.recorder.report = True
        with self.assertRaises(Breaker):
            self.recorder.check("line1")

    def test_recorder_check_no_report_back(self):
        """
        Test case to verify that the check method correctly raises a Breaker
        exception when back is True and the input line is the same as the previous line.
        """
        self.recorder.previous["back"] = True
        with self.assertRaises(Breaker):
            self.recorder.check("line1")

    def test_recorder_check_different_line(self):
        """
        Test case to verify that the check method correctly sets
        report to False when the input line is different from the previous line.
        """
        self.recorder.check("line2")
        self.assertEqual(self.recorder.report, False)


if __name__ == "__main__":
    unittest.main()
