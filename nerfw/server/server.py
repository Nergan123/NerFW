from flask import Flask, request, jsonify, render_template, make_response

from nerfw.game.generator.script import Script
from nerfw.server.Renderer import Renderer
from nerfw.server.wrapper import FlaskAppWrapper


class Server:
    """Server class"""

    def __init__(self, script: Script):
        self.script = script.get_script()
        flask_app = Flask(__name__)
        self.app = FlaskAppWrapper(flask_app)
        self.renderer = Renderer()

    @staticmethod
    def home():
        """
        Renders home url
        :return: Rendered template from html
        """

        resp = make_response(render_template("index.html"))
        resp.set_cookie("line_id", "0")
        return resp

    def forward(self):
        """
        Test function
        :return:
        """

        line_id = int(request.cookies.get("line_id"))
        next_scene = self.script[line_id + 1]
        next_scene = self.renderer.render(next_scene)

        resp = make_response(jsonify(result=next_scene))
        resp.set_cookie("line_id", f"{line_id + 1}")

        return resp

    def run(self, debug=False):
        """
        Runs a server

        :return: None
        """

        self.app.add_endpoint('/forward', 'forward', self.forward, methods=['POST'])
        self.app.add_endpoint('/', 'home', self.home, methods=['GET'])
        self.app.run(debug=debug)
