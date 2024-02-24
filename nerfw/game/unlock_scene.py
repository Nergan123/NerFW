import sqlite3

from nerfw.helpers.db_handler import DbHandler
from nerfw.helpers.img_handler import ImageHandler
from nerfw.helpers.logger import LoggerBase


class UnlockScene(LoggerBase):
    """
    Class to unlock scenes
    """

    def __init__(self):
        super().__init__()
        self.db = DbHandler()
        self.img_handler = ImageHandler()

    def unlock(self, image: str, username: str, label: str, category: str):
        """
        Unlocks a scene

        :param image: Path to image
        :param username: Username
        :param label: Label for the image
        :param category: Category of the image
        :return: None
        """

        self.logger.debug(f"Unlocking scene: {image}")
        binary = self.img_handler.convert_to_base64(image)
        query = ("INSERT INTO unlockedScenes (sceneId, user, label, image, category) "
                 "VALUES (?, ?, ?, ?, ?)")
        values = [(username + label), username, label, binary, category]

        try:
            self.db.execute(query, values)
        except sqlite3.IntegrityError:
            self.logger.debug(f" {username} has already unlocked {image}")
