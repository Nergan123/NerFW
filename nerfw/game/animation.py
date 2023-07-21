import io

from nerfw.helpers.logger import LoggerBase


class Animations(LoggerBase):
    """
    Class for handling animations
    """

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.current_x = pos_x
        self.current_y = pos_y
        self.css = ""

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

        text = io.StringIO()
        text.write(f"--moveStartX: {self.current_x}%;")
        text.write(f"--moveEndX: {move_x}%;")
        text.write(f"--moveStartY: {self.current_y}%;")
        text.write(f"--moveEndY: {move_y}%;")
        text.write(f"animation: {duration}s ease-in-out 0s 1 slideIn;")

        self.current_x = move_x
        self.current_y = move_y

        self.css = text.getvalue()
