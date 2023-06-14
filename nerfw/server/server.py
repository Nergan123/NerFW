from flask import Flask, request, jsonify, render_template, make_response, redirect

from nerfw.helpers.breaker import Breaker
from nerfw.helpers.errors.user_doesnt_exist import UserDoesntExist
from nerfw.helpers.input_handler import InputHandler
from nerfw.server.login_handler import LoginHandler
from nerfw.server.renderer import Renderer
from nerfw.server.saves_handler import SavesHandler
from nerfw.server.wrapper import FlaskAppWrapper
from nerfw.ui.menus import Menus
from nerfw.ui.ui import Ui


class Server:
    """Server class"""

    def __init__(self, ui: Ui):
        flask_app = Flask(__name__)
        self.app = FlaskAppWrapper(flask_app)
        self.renderer = Renderer(ui)
        self.input = InputHandler("", "")
        self.saves_handler = SavesHandler()
        self.login_handler = LoginHandler()
        self.script = None

    def home(self):
        """
        Renders home url
        :return: Rendered template from html
        """

        login = request.cookies.get("login")

        if login is None:
            return redirect("/login")

        html, css = self.renderer.render_menu(self.renderer.ui.main_menu)
        resp = make_response(render_template("test.html", html=html, css=css))
        self.input.reset()
        resp.set_cookie("line", self.input.get_current_line())
        resp.set_cookie("prev_line", self.input.get_prev_line())

        return resp

    def login(self):
        """
        Login page
        :return: Login page
        """

        if request.method == "POST":
            data = request.form.to_dict(flat=False)
            try:
                self.login_handler.login(data)
            except UserDoesntExist:
                resp = make_response(redirect("/"))
                resp.set_cookie("login", "test")
                return resp
            resp = make_response(redirect("/"))
            resp.set_cookie("line", self.input.get_current_line())
            resp.set_cookie("prev_line", self.input.get_prev_line())
        else:
            html, css = self.renderer.render_menu(self.renderer.ui.login_menu)
            resp = make_response(render_template("test.html", html=html, css=css))

        return resp

    def game(self):
        """
        Game page
        :return: Rendered template for game
        """

        html, css = self.renderer.render_menu(self.renderer.ui.dialogue_window)
        resp = make_response(render_template("test.html", html=html, css=css))

        resp.set_cookie("line", self.input.get_current_line())
        resp.set_cookie("prev_line", self.input.get_prev_line())

        return resp

    def backward(self):
        """
        Returns to previous slide
        :return:
        """

        line = request.cookies.get("prev_line")
        try:
            self.script(line)
            html = ""
            css = ""
            text = ""
        except Breaker as br:
            html, css = self.renderer.render(br, Menus.DIALOGUE)
            text = br.line

        resp = make_response(jsonify(html=html, css=css))
        self.input.set_line(text)
        resp.set_cookie("line", self.input.get_current_line())
        resp.set_cookie("prev_line", self.input.get_prev_line())

        return resp

    def forward(self):
        """
        Progresses the game forward function
        :return:
        """

        line = request.cookies.get("line")
        try:
            self.script(line)
            html = ""
            css = ""
            text = ""
        except Breaker as br:
            html, css = self.renderer.render(br, Menus.DIALOGUE)
            text = br.line

        resp = make_response(jsonify(html=html, css=css))
        self.input.set_line(text)
        resp.set_cookie("line", self.input.get_current_line())
        resp.set_cookie("prev_line", self.input.get_prev_line())

        return resp

    def run(self, script, debug=False):
        """
        Runs a server

        :param debug: Sets debug mode
        :param script: Script to be run
        :return: None
        """

        self.script = script
        try:
            self.script(self.input.get_current_line())
        except Breaker:
            pass

        self.app.add_endpoint('/forward', 'forward', self.forward, methods=['POST'])
        self.app.add_endpoint('/backward', 'backward', self.backward, methods=['POST'])
        self.app.add_endpoint('/game', 'game', self.game, methods=['GET'])
        self.app.add_endpoint('/login', 'login', self.login, methods=['GET', 'POST'])
        self.app.add_endpoint('/', 'home', self.home, methods=['GET'])
        self.app.run(host="0.0.0.0", debug=debug)
