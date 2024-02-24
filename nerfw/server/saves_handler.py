import json

from nerfw.helpers.logger import LoggerBase
from nerfw.helpers.db_handler import DbHandler


class SavesHandler(LoggerBase):
    """
    Class for handling saves files
    """

    def __init__(self):
        super().__init__()
        self.db = DbHandler()

    def create_save(self, login: str, data: dict):
        """
        Creates an entry in database

        :param login: User login
        :param data: Save data
        :return: None
        """

        self.logger.debug(f"Creating save for: {login}")
        sql = "INSERT INTO saves(login, date, data) VALUES(?, DATETIME('now','localtime'), ?)"
        data = {
            "line": data["line"],
            "prev_line": data["prev_line"]
        }
        text = json.dumps(data)
        values = [login, text]

        self.db.execute(sql, values)

    def get_all_saves(self, login: str):
        """
        Gets all save files for Login

        :param login: user login
        :return: list of saves
        """

        sql = "SELECT date, data FROM saves WHERE login = ?"
        values = [login]

        self.logger.debug(f"Requesting all saves for: {login}")
        result = self.db.execute(sql, values)

        return result
