from flask import request, abort

from app.core.configs import Config
from app.core.utils import parse_data, validate_data


def fixes_endpoint(num, body):

    config = Config()

    json_data = parse_data(request)
    validate_data(json_data)

    # response = body, 201 # --> Not using as forces boolean to string due to spec not allowing 'mixed' types
    response = json_data, 201
    data_msg = json_data.get("set_message", None)

    if num != "1":
        abort(400, "Valid id range: 1-1")

    if not data_msg:
        config._message = None
        return response

    config._message = data_msg

    return response
