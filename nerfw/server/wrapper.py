from nerfw.server.token_handler import TokenHandler


class FlaskAppWrapper:
    """
    Wrapper for a flask app
    Configures the server
    """

    def __init__(self, app, **configs):
        self.app = app
        self.config = {}
        self.configs(**configs)
        self.app.secret_key = TokenHandler().get_key()

    def configs(self, **configs):
        """
        Adds configs to the app

        :param configs: Configurations for the server
        :return: None
        """
        for config, value in configs:
            self.app.config[config.upper()] = value

    def add_endpoint(
        self,
        endpoint=None,
        endpoint_name=None,
        handler=None,
        methods=None,
        *args,
        **kwargs
    ):
        """
        Adds server url endpoints

        :param endpoint: url
        :param endpoint_name: name for the endpoint
        :param handler: Function which is called
        :param methods: Web methods
        :param args: arguments which are passed to the function
        :param kwargs: positional args which are passed to function
        :return: None
        """
        if methods is None:
            methods = ["GET"]
        self.app.add_url_rule(
            endpoint, endpoint_name, handler, methods=methods, *args, **kwargs
        )

    def run(self, **kwargs):
        """
        Runs a server

        :param kwargs: Positional arguments passed to the app
        :return: None
        """
        self.app.run(**kwargs)
