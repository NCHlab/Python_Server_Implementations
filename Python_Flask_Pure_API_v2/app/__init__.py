import os, sys
from dotenv import load_dotenv
from flask import Flask, request, abort

from app.core import error_handlers
from app.routes.hello import hello_route
from app.routes.tests import tests_route
from app.routes.fixes import fixes_route


sys.path.append(os.path.dirname(os.path.realpath(__file__)))


def create_app():

    load_dotenv()

    app = Flask(__name__)
    app.register_blueprint(error_handlers.blueprint)
    app.register_blueprint(hello_route)
    app.register_blueprint(tests_route)
    app.register_blueprint(fixes_route)

    return app
