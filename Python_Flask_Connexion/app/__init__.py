import connexion
import os
from app.core import error_handlers


def create_app():

    try:
        OPENAPI_SPEC_PATH = os.environ["OPENAPI_SPEC_PATH"]
    except KeyError:
        OPENAPI_SPEC_PATH = "../openapi/"

    app = connexion.FlaskApp(__name__, specification_dir=OPENAPI_SPEC_PATH)
    # app = connexion.App(__name__, specification_dir=spec_path)
    app.add_api("spec.yml", strict_validation=True)
    app.app.register_blueprint(error_handlers.blueprint)

    return app.app
