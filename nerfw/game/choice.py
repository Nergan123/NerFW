from nerfw.helpers.logger import LoggerBase


class Choice(LoggerBase):
    """
    Class for creating a choice menu
    """

    def __init__(self, recorder=None, choices=None, cookies=None, choice_id=None):
        super().__init__()
        self.id = str(choice_id)
        if choices is None:
            choices = []
        self.recorder = recorder
        self.choices = choices
        self.answers = None
        self.cookies = cookies
        self.setup()

    def setup(self):
        """
        Sets up choice from cookies
        :return: None
        """

        try:
            self.logger.debug(f"Found existing answers: {self.cookies['choices'][self.id]}")
            self.answers = []
            for choice in self.choices:
                if choice == self.cookies["choices"][self.id]:
                    self.answers.append(True)
                else:
                    self.answers.append(False)
        except KeyError:
            self.answers = []

    def make(self):
        """
        Displays or passes a choice
        :return: answers
        """

        self.recorder.check(str(self.choices))
        self.recorder.scene.remove_choice_from_scene()
        return self.answers

    def compile(self):
        """
        Compiles css and html
        :return: css, html
        """

        html = "<div class='big_wrapper'>"
        html += "<div class='choice'>"
        for choice in self.choices:
            html += f"<button class='button_specific' id='{self.id}' value='{choice}' " \
                    f"onclick='RegisterChoice(this)'>{choice}</button>"
        html += "</div>"
        html += "</div>"

        return html
