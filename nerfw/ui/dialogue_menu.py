from nerfw.ui.functions import Functions
from nerfw.ui.ui_base import UiBase


class DialogueWindow(UiBase):
    """
    Class for dialogue window ui
    """

    def __init__(self):
        super().__init__()
        self.id = "dialogue_menu"
        self.setup()

    def setup(self):
        """
        Sets up a ui
        :return: None
        """

        self.add_text_field("char-name", (5, 5), 20)
        self.add_text_field("char-text", (5, 12), 20)
        self.add_button("next", (15, 85), Functions.FORWARD)
        self.add_button("back", (5, 85), Functions.BACKWARD)
        self.add_button("main_menu", (70, 85), Functions.REDIRECT_MAIN_PAGE)
        self.add_button("save", (85, 85), Functions.SAVE)
