from flask import Flask, request, jsonify, render_template, make_response

from nerfw.helpers.breaker import Breaker
from nerfw.server.Renderer import Renderer
from nerfw.server.wrapper import FlaskAppWrapper


class Server:
    """Server class"""

    def __init__(self):
        flask_app = Flask(__name__)
        self.app = FlaskAppWrapper(flask_app)
        self.renderer = Renderer()
        self.script = None

    @staticmethod
    def home():
        """
        Renders home url
        :return: Rendered template from html
        """

        resp = make_response(render_template("index.html"))
        resp.set_cookie("line", "")
        return resp

    def forward(self):
        """
        Test function
        :return:
        """

        line = request.cookies.get("line")
        try:
            self.script(line)
            next_scene = {
                "line": {
                    "name": "Game Over",
                    "text": "Restart"
                }
            }
        except Breaker as line_to_return:
            line = line_to_return
            next_scene = {
                "line": {
                    "name": line.name,
                    "text": line.line
                }
            }

        rendered_scene = self.renderer.render(next_scene)
        resp = make_response(jsonify(result=rendered_scene))
        resp.set_cookie("line", next_scene["line"]["text"])

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
            self.script("")
        except Breaker:
            pass
        self.app.add_endpoint('/forward', 'forward', self.forward, methods=['POST'])
        self.app.add_endpoint('/', 'home', self.home, methods=['GET'])
        self.app.run(debug=debug)
