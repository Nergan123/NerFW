import json
import unittest
from unittest.mock import Mock
from nerfw.game.string_input import StringInput
from nerfw.helpers.recorder import Recorder


class TestStringInput(unittest.TestCase):
    """
    Test cases for string input class
    """
    def test_string_input_initialization_with_valid_parameters(self):
        """
        Testing initialization with valid parameters
        """
        string_input = StringInput(
            recorder=Mock(), cookies={}, string="Test", string_id=1
        )
        self.assertEqual(string_input.answer, "")

    def test_string_input_initialization_without_parameters(self):
        """
        Testing initialization without parameters
        """
        with self.assertRaises(TypeError):
            StringInput()

    def test_string_input_setup_with_existing_string(self):
        """
        Testing setup with existing string
        """
        cookies = {"stringInput": {"1": "Test"}}
        string_input = StringInput(cookies=cookies, string_id=1)
        self.assertEqual(string_input.answer, "Test")

    def test_string_input_setup_without_existing_string(self):
        """
        Testing setup without existing string
        """
        cookies = {"stringInput": {}}
        string_input = StringInput(cookies=cookies, string_id=1)
        self.assertEqual(string_input.answer, "")

    def test_string_input_make(self):
        """
        Testing make method
        """
        line = '{"line": "Test1", "back": false, "choices": {}, "stringInput": {}}'
        recorder = Recorder(last_line=line, scene=Mock())
        string_input = StringInput(
            recorder=recorder, cookies=json.loads(line), string="Test", string_id=1
        )
        self.assertEqual(string_input.make(), "")

    def test_string_input_to_dict(self):
        """
        Testing to_dict method
        """
        line = {"line": "Test1", "back": False, "choices": {}, "stringInput": {}}
        string_input = StringInput(Mock(), line, string="Test", string_id=1)
        output = string_input.to_dict()
        expected_output = {"id": 1, "text": "Test"}
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
