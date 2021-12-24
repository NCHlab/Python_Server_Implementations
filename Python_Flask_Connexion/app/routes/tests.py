from flask import request, abort

from app.core.configs import Config
from app.core.utils import parse_data, validate_data


def tests_endpoint(body):

    config = Config()
    msg = config._message

    response = "", 204

    json_data = parse_data(request)
    validate_data(json_data)

    if len(body) != 1:
        abort(400, "Only 'set_message' allowed in body")

    # As a result of connexion handling some bad params, can assume set_message is in body
    config._message = body["set_message"]

    return response
