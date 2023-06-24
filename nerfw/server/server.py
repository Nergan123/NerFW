import re

from flask import Flask, request, jsonify, render_template, make_response, redirect

from nerfw.helpers.breaker import Breaker
from nerfw.helpers.errors.password_mismatch import PasswordsMismatch
from nerfw.helpers.errors.user_already_registered import UserAlreadyRegistered
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
                resp = make_response(redirect("/"))
                resp.set_cookie("login", data["Login"][0])
                resp.set_cookie("line", self.input.get_current_line())
                resp.set_cookie("prev_line", self.input.get_prev_line())
            except UserDoesntExist:
                resp = make_response(redirect("/login/register"))
        else:
            html, css = self.renderer.render_menu(self.renderer.ui.login_menu)
            resp = make_response(render_template("test.html", html=html, css=css))

        return resp

    def register(self):
        """
        Registers a user
        :return: Register page
        """

        if request.method == "POST":
            data = request.form.to_dict(flat=False)
            try:
                self.login_handler.register(data)
                resp = make_response(redirect("/login"))
            except UserAlreadyRegistered:
                resp = make_response(redirect("/login"))
            except PasswordsMismatch:
                resp = make_response(redirect("/login/register"))
                resp.set_cookie("error", "Password mismatch")
        else:
            html, css = self.renderer.render_menu(self.renderer.ui.register_menu)
            error = request.cookies.get("error")
            if error is None:
                error = ""
            template = render_template("test.html", html=html, css=css)
            template = re.sub(r"\{\{ text\|safe }}", error, template)
            resp = make_response(template)
            resp.delete_cookie("error")

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
        :return: None
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
        :return: None
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

    def save(self):
        """
        Creates a save entry in db
        :return: None
        """

        data = request.cookies.to_dict()
        self.saves_handler.create_save(data["login"], data)
        resp = make_response(jsonify(code=200))
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

        self.app.add_endpoint('/', 'home', self.home, methods=['GET'])
        self.app.add_endpoint('/game', 'game', self.game, methods=['GET'])
        self.app.add_endpoint('/game/forward', 'forward', self.forward, methods=['POST'])
        self.app.add_endpoint('/game/backward', 'backward', self.backward, methods=['POST'])
        self.app.add_endpoint('/game/save', 'save', self.save, methods=['POST'])
        self.app.add_endpoint('/login', 'login', self.login, methods=['GET', 'POST'])
        self.app.add_endpoint('/login/register', 'register', self.register, methods=['GET', 'POST'])
        self.app.run(host="0.0.0.0", debug=debug)
