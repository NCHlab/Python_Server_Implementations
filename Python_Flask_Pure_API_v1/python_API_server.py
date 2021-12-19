from dotenv import load_dotenv
from flask import Flask, request, abort

import error_handlers
from configs import Config
from utils import validate_auth, parse_data, validate_data

app = Flask(__name__)
app.register_blueprint(error_handlers.blueprint)
load_dotenv()


@app.route("/hello", methods=["GET"])
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


@app.route("/tests", methods=["POST"])
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


@app.route("/fixes/id/<num>", methods=["PUT"])
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4004)
