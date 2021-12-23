import os
from flask import abort


# def validate_auth(req, auth_type):
#     header_auth = req.headers.get("Authorization", None)
#     auth = os.environ.get(auth_type)

#     if not header_auth or header_auth != auth:
#         abort(401)


# def parse_data(req):

#     json_data = None

#     if req.is_json:
#         try:
#             json_data = req.get_json()
#         except Exception:
#             # Case where content-type is sent as json but no data
#             abort(400, "Data must be sent as JSON")

#     return json_data


# def validate_data(json_data):
#     # if json not submitted
#     if not json_data:
#         abort(400, "Data must be sent as JSON")
