from flask import Flask, request, jsonify, render_template, make_response

from nerfw.helpers.breaker import Breaker
from nerfw.server.renderer import Renderer
from nerfw.server.wrapper import FlaskAppWrapper
from nerfw.ui.ui import Ui


class Server:
    """Server class"""

    def __init__(self, ui: Ui):
        flask_app = Flask(__name__)
        self.app = FlaskAppWrapper(flask_app)
        self.renderer = Renderer(ui)
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
            html = ""
            css = ""
            text = ""
        except Breaker as br:
            html, css = self.renderer.render(br)
            text = br.line

        resp = make_response(jsonify(html=html, css=css))
        resp.set_cookie("line", text)

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
        self.app.run(host="0.0.0.0", debug=debug)
