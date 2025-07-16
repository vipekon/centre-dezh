from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)

    app.secret_key = Config.SECRET_KEY

    from .routes_main import bp as main_bp
    from .routes_api import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app