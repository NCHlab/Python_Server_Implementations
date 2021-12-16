# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

import os
from dotenv import load_dotenv
from flask import Flask, request, abort, make_response

app = Flask(__name__)
load_dotenv()


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    def __init__(self):
        self._message = None


@app.route("/hello", methods=["GET"])
def hello_endpoint():

    config = Config()
    message = config._message
    param = request.args.get("message", None)
    response = param, 200

    if len(request.args) > 1 or param is None:
        abort(400)

    if message:
        response = param, 200, {"set_message": message}

    return response


@app.route("/tests", methods=["POST"])
def tests_endpoint():

    config = Config()
    form_length = len(request.form)
    data = request.form.get("set_message", None)
    header_auth = request.headers.get("Authorization", None)
    auth = os.environ.get("BASIC_AUTHENTICATION")

    if not header_auth:
        abort(403)

    elif header_auth != auth:
        abort(401)

    if not data and data != "" or form_length > 1:
        abort(400)

    response = "", 200
    config._message = data

    return response


@app.route("/fixes/id/<num>", methods=["PUT"])
def fixes_endpoint(num):

    config = Config()
    auth = os.environ.get("OAUTH_AUTHENTICATION")
    header_auth = request.headers.get("Authorization", None)
    data = request.form.get("set_message", None)
    all_data = request.form

    if not header_auth:
        abort(403)

    elif header_auth != auth:
        abort(401)

    elif num != "1":
        abort(400)

    if not all_data:
        abort(400)
    else:
        format_data = ["{}={}".format(key, all_data[key]) for key in all_data]
        response = make_response("\n".join(format_data), 201)

    if not data or data == "False":
        config._message = None
        return response

    config._message = data
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4004)
