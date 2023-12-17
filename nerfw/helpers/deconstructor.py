from nerfw.helpers.logger import LoggerBase
from nerfw.helpers.breaker import Breaker
from nerfw.helpers.img_handler import ImageHandler


class Deconstructor(LoggerBase):
    """Class for scene deconstruction"""

    def __init__(self):
        super().__init__()
        self.image_handler = ImageHandler()

    def deconstruct(self, breaker: Breaker):
        """
        Deconstructs Breaker exception into json
        :param breaker: Exception to deconstruct
        :return: Dict
        """

        if breaker.scene.choice is not None:
            choice = breaker.scene.choice.to_dict()
        else:
            choice = {}

        self.logger.debug(f"Deconstructing: {breaker}")
        scene_dict = {
            "background": breaker.scene.background,
            "characters": [character.to_dict() for character in breaker.scene.characters_to_show],
            "text": breaker.line,
            "name": breaker.scene.name,
            "choice": choice,
            "audio": breaker.scene.audio
        }

        return scene_dict
