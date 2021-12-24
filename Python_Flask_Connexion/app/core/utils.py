import os
from flask import abort


def parse_data(req):

    json_data = None

    # Checks Content-Type is application/json
    if req.is_json:
        try:
            json_data = req.get_json()
        except Exception:
            # Case where content-type is sent as json but no data
            abort(400, "Data must be sent as JSON")

    return json_data


def validate_data(json_data):
    # if json not submitted
    if not json_data:
        abort(400, "Data must be sent as JSON")
