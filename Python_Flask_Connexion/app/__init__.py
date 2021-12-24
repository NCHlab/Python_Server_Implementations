import os
import connexion

from app.core.validators import RequestBodyValidator
from app.core import error_handlers


def create_app():

    try:
        OPENAPI_SPEC_PATH = os.environ["OPENAPI_SPEC_PATH"]
    except KeyError:
        OPENAPI_SPEC_PATH = "../openapi/"

    app = connexion.FlaskApp(__name__, specification_dir=OPENAPI_SPEC_PATH)
    app.add_api(
        "spec.yml", validator_map={"body": RequestBodyValidator}, strict_validation=True
    )

    app.add_error_handler(400, error_handlers.method_not_allowed_400)
    app.add_error_handler(401, error_handlers.method_not_allowed_401)
    app.add_error_handler(405, error_handlers.method_not_allowed_405)

    return app.app
