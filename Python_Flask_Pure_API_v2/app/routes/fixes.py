from flask import Blueprint, request, abort
from app.core.configs import Config
from app.core.utils import validate_auth, parse_data, validate_data

fixes_route = Blueprint("fixes_route", __name__)


@fixes_route.route("/fixes/id/<num>", methods=["PUT"])
def fixes_endpoint(num):

    config = Config()

    validate_auth(request, "OAUTH_AUTHENTICATION")
    json_data = parse_data(request)
    validate_data(json_data)

    if num != "1":
        abort(400, "Valid id range: 1-1")

    data_msg = json_data.get("set_message", None)
    response = json_data, 201

    if not data_msg:
        config._message = None
        return response

    config._message = data_msg
    return response
