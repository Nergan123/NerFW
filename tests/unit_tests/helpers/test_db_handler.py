import unittest
from unittest.mock import MagicMock, patch
from nerfw.helpers.db_handler import DbHandler


class DbHandlerTests(unittest.TestCase):
    """
    Unit test class for the DbHandler class in the nerfw.helpers.db_handler module.
    """

    # pylint: disable=arguments-differ
    @patch("sqlite3.connect")
    def setUp(self, mock_connect):
        """
        Set up method for the test class. Initializes an instance of the DbHandler class.
        """
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        self.db_handler = DbHandler()

    def test_db_handler_initialization(self):
        """
        Test case to verify that the DbHandler class is correctly initialized.
        """
        self.assertIsInstance(self.db_handler, DbHandler)

    def test_db_handler_setup_db(self):
        """
        Test case to verify that the setup_db method correctly sets up the database.
        """
        self.db_handler.setup_db()
        self.db_handler.connection.cursor().execute.assert_called()

    def test_db_handler_execute_no_values(self):
        """
        Test case to verify that the execute method correctly executes a SQL command without values.
        """
        self.db_handler.execute("SELECT * FROM saves")
        self.db_handler.connection.cursor().execute.assert_called_with(
            "SELECT * FROM saves"
        )

    def test_db_handler_execute_with_values(self):
        """
        Test case to verify that the execute method correctly executes a SQL command with values.
        """
        self.db_handler.execute("SELECT * FROM saves WHERE login = ?", ("test_user",))
        self.db_handler.connection.cursor().execute.assert_called_with(
            "SELECT * FROM saves WHERE login = ?", ("test_user",)
        )


if __name__ == "__main__":
    unittest.main()
