from nerfw.helpers.logger import LoggerBase


class Animations(LoggerBase):
    """
    Class for handling animations
    """

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.current_x = pos_x
        self.current_y = pos_y
        self.css = {}

    def move(self, move_x: int, move_y: int, duration: float or int):
        """
        Moves character

        :param move_x: Translation by X axis
        :param move_y: Translation by Y axis
        :param duration: Duration of animation in seconds
        :return:
        """

        self.logger.debug(f"Moving from {self.current_x} to {move_x} by X\n"
                          f"Moving from {self.current_y} to {move_y} by Y")

        css = {
            "position": "absolute",
            "--moveStartX": f"{self.current_x}%",
            "--moveEndX": f"{move_x}%",
            "--moveStartY": f"{self.current_y}%",
            "--moveEndY": f"{move_y}%",
            "animation": f"{duration}s ease-in-out 0s 1 slideIn",
            "top": f"{move_y}%",
            "left": f"{move_x}%",
            "overflow": "hidden",
        }

        self.current_x = move_x
        self.current_y = move_y

        self.css = css
