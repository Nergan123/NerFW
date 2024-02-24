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

        self.logger.debug(f"Deconstructing: {breaker}")
        scene_dict = {
            "background": breaker.scene.background,
            "characters": [
                character.to_dict() for character in breaker.scene.characters_to_show
            ],
            "text": breaker.line,
            "name": breaker.scene.name,
            "color": breaker.scene.color,
            "choice": {}
            if breaker.scene.choice is None
            else breaker.scene.choice.to_dict(),
            "stringInput": {}
            if breaker.scene.string_input is None
            else breaker.scene.string_input.to_dict(),
            "audio": breaker.scene.audio,
        }

        return scene_dict
