import sqlite3

from nerfw.helpers import LoggerBase


class DbHandler(LoggerBase):
    """
    Handler for database
    """

    def __init__(self):
        super().__init__()
        self.path = "login_data.db"
        self.connection = sqlite3.connect(self.path)
        try:
            self.setup_db()
        except sqlite3.OperationalError:
            pass

    def setup_db(self):
        """
        Sets up databases
        :return:
        """

        with self.connection:
            cur = self.connection.cursor()
            cur.execute("CREATE TABLE saves (login TEXT, date TEXT, data TEXT);")

    def execute(self, query: str, values=None):
        """
        Executes sql query
        :param query: Query to execute
        :param values: Values if have
        :return: list
        """

        with self.connection:
            cur = self.connection.cursor()
            if values is None:
                cur.execute(query)
            else:
                cur.execute(query, values)

        return cur.fetchall()
