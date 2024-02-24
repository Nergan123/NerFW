from nerfw.helpers.db_handler import DbHandler
from nerfw.helpers.img_handler import ImageHandler
from nerfw.helpers.logger import LoggerBase


class Gallery(LoggerBase):
    """
    Class to handle gallery
    """

    def __init__(self):
        super().__init__()
        self.img_handler = ImageHandler()
        self.db = DbHandler()

    def get_images(self, username: str):
        """
        Gets images for the user

        :param username: Username
        :return: list
        """

        self.logger.debug(f"Getting images for {username}")
        query = "SELECT image, category, label FROM unlockedScenes WHERE user = ?"
        result = self.db.execute(query, [username])
        self.logger.debug(f"Images for {username}: {result}")
        return result
