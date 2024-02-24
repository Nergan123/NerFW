import sqlite3

from nerfw.helpers.logger import LoggerBase


class DbHandler(LoggerBase):
    """
    Handler for database
    """

    def __init__(self):
        super().__init__()
        self.path = "login_data.db"
        self.connection = sqlite3.connect(self.path, check_same_thread=False)
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
            cur.execute(
                "CREATE TABLE IF NOT EXISTS saves (login TEXT, date TEXT, data TEXT);"
            )
            cur.execute(
                "CREATE TABLE IF NOT EXISTS credentials"
                "(login TEXT, password TEXT, salt TEXT, UNIQUE(login));"
            )
            cur.execute(
                "CREATE TABLE IF NOT EXISTS unlockedScenes "
                "(sceneId TEXT, user TEXT, label TEXT, image TEXT, "
                "category TEXT, "
                "date DATETIME DEFAULT CURRENT_TIMESTAMP, "
                "UNIQUE(sceneId));"
            )

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
