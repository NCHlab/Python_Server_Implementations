from flask import Flask
from app.routes import api
from app.core import error_handlers


def create_app():

    app = Flask(__name__)
    api.init_app(app)

    return app
