from flask import Blueprint, request, abort
from app.core.configs import Config

hello_route = Blueprint("hello_route", __name__)


@hello_route.route("/hello", methods=["GET"])
def hello_endpoint():

    config = Config()
    message = config._message

    param = request.args.get("message", None)
    response = {"message": param}, 200

    if len(request.args) > 1 or param is None:
        abort(400, "Only one query allowed, 'message'")

    elif message:
        response = {"message": param}, 200, {"set_message": message}

    return response
