from flask import Blueprint, request, abort
from app.core.configs import Config
from app.core.utils import validate_auth, parse_data, validate_data

tests_route = Blueprint("tests_route", __name__)


@tests_route.route("/tests", methods=["POST"])
def tests_endpoint():

    config = Config()

    validate_auth(request, "BASIC_AUTHENTICATION")
    json_data = parse_data(request)
    validate_data(json_data)

    data_msg = json_data.get("set_message", None)

    if not data_msg or len(json_data) > 1:
        abort(400, "Only 'set_message' allowed in body")

    response = "", 200
    config._message = data_msg

    return response
