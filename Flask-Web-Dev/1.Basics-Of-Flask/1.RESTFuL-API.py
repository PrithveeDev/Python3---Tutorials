from flask import Flask, jsonify, request
app = Flask(__name__)


class FlaskWebApp(flask):
    __Languages = [{'Name': 'Python', 'Type': 'Dynamically Typed'}, {'Name': 'C', 'Type': 'Statically Typed'}]

    def __init__(self, port: int, host: str, debg: bool, appf, import_name: str):
        try:
            assert isinstance(port, int), f"Port: {port} isn't an instance of Integer Class."
            assert isinstance(host, str), f"Host: {host} isn't an instance of String Class."
            assert isinstance(debg, bool), f"Debug: {debg} isn't an instance of Boolean Class."
        except AssertionError:
            print("Bad Input To Class.")
        else:
            self.port = port
            self.host = host
            self.debg = debg
            self.appf = appf

    @app.route('/', methods=['GET'])
    def root_dir(self):
        return '<h1> Main - Page </h1>'

    @app.route('/Languages-Supported', methods=['GET'])
    def lang_dir(self):
        pass

    @app.route('/Languages-Supported/Add-One/<string:name>', methods=['POST'])
    def add_lang(self, name):
        pass

    def start_server(self):
        self.appf.run(port=self.port, host=self.host, debug=self.debg)


if __name__ == "__main__":
    FlaskApp = FlaskWebApp(5000, '0.0.0.0', True, app)
    FlaskApp.start_server()
