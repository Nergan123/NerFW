import unittest
from unittest.mock import patch
from nerfw.server.saves_handler import SavesHandler


class SavesHandlerTests(unittest.TestCase):
    """
    This class contains unit tests for the SavesHandler class.
    """

    def setUp(self):
        """
        This method is called before each test. It initializes the SavesHandler object.
        """
        self.saves_handler = SavesHandler()

    @patch("nerfw.helpers.db_handler.DbHandler.execute")
    def test_saves_creation_success(self, mock_execute):
        """
        This test checks if the save creation method
        successfully creates a save when the database operation is successful.
        """
        mock_execute.return_value = None
        self.saves_handler.create_save(
            "test_user", {"line": "test_line", "prev_line": "test_prev_line"}
        )

    @patch("nerfw.helpers.db_handler.DbHandler.execute")
    def test_saves_creation_failure(self, mock_execute):
        """
        This test checks if the save creation method
        raises an exception when the database operation fails.
        """
        mock_execute.side_effect = Exception("Database error")
        with self.assertRaises(Exception):
            self.saves_handler.create_save(
                "test_user", {"line": "test_line", "prev_line": "test_prev_line"}
            )

    @patch("nerfw.helpers.db_handler.DbHandler.execute")
    def test_get_all_saves_success(self, mock_execute):
        """
        This test checks if the get all saves method successfully
        retrieves all saves when the database operation is successful.
        """
        mock_execute.return_value = [("date1", "data1"), ("date2", "data2")]
        result = self.saves_handler.get_all_saves("test_user")
        self.assertEqual(result, [("date1", "data1"), ("date2", "data2")])

    @patch("nerfw.helpers.db_handler.DbHandler.execute")
    def test_get_all_saves_failure(self, mock_execute):
        """
        This test checks if the get all saves method raises
        an exception when the database operation fails.
        """
        mock_execute.side_effect = Exception("Database error")
        with self.assertRaises(Exception):
            self.saves_handler.get_all_saves("test_user")


if __name__ == "__main__":
    unittest.main()
