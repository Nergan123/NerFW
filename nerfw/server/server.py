import json
import datetime
import logging
from json import loads

from authlib.integrations.flask_client import OAuth
from flask import Flask, request, jsonify, render_template, make_response, redirect
from nerfw.helpers.deconstructor import Deconstructor

from nerfw.helpers.breaker import Breaker
from nerfw.helpers.errors.password_mismatch import PasswordsMismatch
from nerfw.helpers.errors.user_already_registered import UserAlreadyRegistered
from nerfw.helpers.errors.user_doesnt_exist import UserDoesntExist
from nerfw.helpers.errors.user_not_allowed import UserNotAllowed
from nerfw.helpers.input_handler import InputHandler
from nerfw.server.gallery import Gallery
from nerfw.server.login_github import LoginGithub
from nerfw.server.login_default import LoginDefault
from nerfw.server.login_patreon import LoginPatreon
from nerfw.server.require_token import require_token
from nerfw.server.saves_handler import SavesHandler
from nerfw.server.token_handler import TokenHandler
from nerfw.server.wrapper import FlaskAppWrapper


class Server:
    """Server class"""

    def __init__(self, login_method: str, name: str):
        flask_app = Flask(
            __name__,
            static_url_path="/",
            static_folder="build",
            template_folder="build",
        )
        self.logger = logging.getLogger(self.__class__.__name__)
        flask_app.errorhandler(404)(lambda e: render_template("index.html"))
        self.app = FlaskAppWrapper(flask_app)
        self.input = InputHandler("", "")
        self.deconstructor = Deconstructor()
        self.saves_handler = SavesHandler()
        self.login_handler = None
        self._set_login_method(login_method)
        self.token_handler = TokenHandler()
        self.gallery_handler = Gallery()
        self.script = None
        self.name = name
        self.background = {"type": "background", "data": "#282a36"}

    def set_background(self, background: dict):
        """
        Sets background

        :param background: Background
        :return: None
        """

        self.background = background

    def _set_login_method(self, method: str):
        """
        Sets login method

        :param method: Login method. Can be "Default", "GitHub"
        :return: None
        """

        if method == "default":
            self.login_handler = LoginDefault()
        elif method == "github":
            oauth = OAuth(self.app)
            self.login_handler = LoginGithub(oauth)
        elif method == "patreon":
            self.login_handler = LoginPatreon()

    def home(self, path: str):
        """
        Renders home url

        :param path: Path
        :return: Rendered template from html
        """

        resp = make_response(render_template("index.html", name_game=self.name))
        if path:
            self.logger.info(f"Path requested: {path}")
        self.input.reset()

        return resp

    def api_authorize(self):
        """
        Login page

        :return: Login page
        """

        if request.method == "GET":
            resp_data = {
                "method": self.login_handler.get_method(),
                "additionalData": self.login_handler.get_additional_data(),
            }
            resp = make_response(resp_data)
            return resp

        data = request.get_json()
        try:
            self.login_handler.login(data)
            resp = make_response()
            token = self.token_handler.create_token(data["Login"])
            expire_date = datetime.datetime.now()
            expire_date = expire_date + datetime.timedelta(days=7)
            resp.set_cookie("token", token, httponly=False, expires=expire_date)
            resp.set_cookie("line", self.input.get_current_line())
            resp.set_cookie("prev_line", self.input.get_prev_line())
        except UserDoesntExist:
            resp = make_response()
            resp.status = 404
        except UserNotAllowed:
            resp = make_response()
            resp.status = 401

        return resp

    def api_register(self):
        """
        Registers a user

        :return: Register page
        """

        data = request.get_json()
        try:
            self.login_handler.register(data)
            resp = make_response()
        except UserAlreadyRegistered:
            resp = make_response()
            resp.status = 409
        except PasswordsMismatch:
            resp = make_response()
            resp.status = 401
            resp.set_cookie("error", "Password mismatch")

        return resp

    @require_token
    def api_backward(self):
        """
        Returns to previous slide

        :return: None
        """

        line = request.cookies.get("prev_line")

        if line is None:
            line = {"line": "", "back": False, "choices": {}, "stringInput": {}}
            line = json.dumps(line)

        resp = make_response()
        resp.set_cookie("line", line)
        self.input.cookie["lines"]["current"] = json.loads(line)
        self.input.cookie["lines"]["previous"] = json.loads(line)

        return resp

    @require_token
    def api_forward(self):
        """
        Progresses the game forward function

        :return: None
        """

        line = request.cookies.get("line")
        username = self.token_handler.unlock_token(request.cookies.get("token"))[
            "login"
        ]
        if line is None:
            line = {"line": "", "back": False, "choices": {}, "stringInput": {}}
        else:
            line = loads(line)

        try:
            answer = request.get_json()["choice"]
            choice_id = request.get_json()["id"]
            line["choices"][choice_id] = answer
        except KeyError:
            pass

        try:
            string_input = request.get_json()["stringInput"]
            input_id = request.get_json()["id"]
            line["stringInput"][str(input_id)] = string_input
        except KeyError:
            pass

        self.input.set_choices(line["choices"])
        self.input.set_string_input(line["stringInput"])
        line = json.dumps(line)

        try:
            self.script(last_line=line, username=username)
            output = redirect("/")
            text = ""
        except Breaker as br:
            output = self.deconstructor.deconstruct(br)
            text = br.line

        resp = make_response(output)
        self.input.set_line(text)
        resp.set_cookie("line", self.input.get_current_line())
        resp.set_cookie("prev_line", self.input.get_prev_line())

        return resp

    @require_token
    def api_get_saves(self):
        """
        Saves menu

        :return: None
        """

        if request.method == "GET":
            login = request.cookies.get("token")
            login = self.token_handler.unlock_token(login)["login"]
            saves = self.saves_handler.get_all_saves(login)

            output = self.render_save(saves, login)

            resp = make_response(output)
            return resp

        data = request.get_json()["data"]
        data = json.loads(data)
        resp = make_response()
        self.input.cookie["lines"]["previous"] = json.loads(data["prev_line"])
        self.input.set_line(json.loads(data["line"])["line"])
        self.input.cookie["lines"]["current"]["back"] = json.loads(data["line"])["back"]
        self.input.cookie["lines"]["current"]["choices"] = json.loads(data["line"])[
            "choices"
        ]

        return resp

    def render_save(self, saves, username):
        """
        Renders scene object for each save

        :param saves: Saves data to render
        :param username: Username
        :return: dict
        """

        output = []

        for date, save in saves:
            line = loads(save)
            line = line["line"]
            try:
                self.script(last_line=line, username=username)
                data = {}
            except Breaker as br:
                data = self.deconstructor.deconstruct(br)
            output.append({"date": date, "data": data, "save": save})

        return output

    @require_token
    def api_create_save(self):
        """
        Creates a save entry in db

        :return: None
        """

        data = request.cookies.to_dict()
        login = self.token_handler.unlock_token(data["token"])["login"]
        self.saves_handler.create_save(login, data)
        resp = make_response()
        return resp

    @require_token
    def api_get_gallery(self):
        """
        Gallery endpoint

        :return: None
        """

        login = request.cookies.get("token")
        login = self.token_handler.unlock_token(login)["login"]
        images = self.gallery_handler.get_images(login)
        images = [
            {"image": img, "category": category, "label": label}
            for img, category, label in images
        ]

        resp = make_response(jsonify(images))
        return resp

    @require_token
    def api_get_background(self):
        """
        Gets background image

        :return: None
        """

        resp = make_response(jsonify(background=self.background))
        return resp

    def run(self, script, debug=False, port=5000):
        """
        Runs a server

        :param debug: Sets debug mode
        :param script: Script to be run
        :param port: Port to be used
        :return: None
        """

        self.script = script
        try:
            self.script(last_line=self.input.get_current_line(), username="")
        except Breaker:
            pass

        self.app.add_endpoint(
            "/", "home", self.home, methods=["GET"], defaults={"path": ""}
        )
        self.app.add_endpoint("/<path:path>", "home", self.home, methods=["GET"])
        self.app.add_endpoint(
            "/api/forward", "forward", self.api_forward, methods=["POST"]
        )
        self.app.add_endpoint(
            "/api/backward", "backward", self.api_backward, methods=["POST"]
        )
        self.app.add_endpoint(
            "/api/save", "save", self.api_create_save, methods=["POST"]
        )
        self.app.add_endpoint(
            "/api/get_saves", "get_saves", self.api_get_saves, methods=["GET", "POST"]
        )
        self.app.add_endpoint(
            "/api/authorize", "authorize", self.api_authorize, methods=["POST", "GET"]
        )
        self.app.add_endpoint(
            "/api/register", "register", self.api_register, methods=["POST"]
        )
        self.app.add_endpoint(
            "/api/gallery", "gallery", self.api_get_gallery, methods=["GET"]
        )
        self.app.add_endpoint(
            "/api/get_background",
            "get_background",
            self.api_get_background,
            methods=["GET"],
        )

        if self.login_handler.get_method() == "github":
            self.app.add_endpoint(
                "/github/callback",
                "github_authorized",
                self.login_handler.authorize,
                methods=["GET"],
            )
        elif self.login_handler.get_method() == "patreon":
            self.app.add_endpoint(
                "/patreon/callback",
                "patreon_authorized",
                self.login_handler.authorize,
                methods=["GET"],
            )

        self.app.run(host="0.0.0.0", debug=debug, port=port)
