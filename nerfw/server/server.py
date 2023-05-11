from flask import Flask, request, jsonify, render_template
from nerfw.server.wrapper import FlaskAppWrapper


class Server:
    """Server class"""

    def __init__(self):
        flask_app = Flask(__name__)
        self.app = FlaskAppWrapper(flask_app)

    @staticmethod
    def action():
        """
        Function which is added to the app
        :return: str
        """

        return "Hello World"

    @staticmethod
    def home():
        """
        Renders home url
        :return: Rendered template from html
        """

        return render_template('home.html')

    @staticmethod
    def test():
        """
        Test function
        :return:
        """
        text1 = request.form['text1']
        text2 = request.form['text2']
        text1 = text1.upper()
        text2 = text2.upper()
        combine = text1 + text2
        result = {
            "output": combine
        }
        result = {str(key): value for key, value in result.items()}
        return jsonify(result=result)

    def run(self, debug=False):
        """
        Runs a server

        :return: None
        """

        self.app.add_endpoint('/action', 'action', self.action, methods=['GET'])
        self.app.add_endpoint('/join', 'test', self.test, methods=['GET', 'POST'])
        self.app.add_endpoint('/', 'home', self.home, methods=['GET'])
        self.app.run(debug=debug)
