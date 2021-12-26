from flask_restx import Namespace, Resource, reqparse
from flask import request, abort
from app.core.configs import Config

api = Namespace("hello", description="Hello Operation")


@api.route("/")
class HelloEndpoint(Resource):
    @api.doc(
        "Hello Endpoint",
        params={
            "message": {
                "description": "Message Value",
                "in": "query",
                "type": str,
                "required": True,
            }
        },
    )
    def get(self):

        config = Config()
        message = config._message

        if len(request.args) > 1:
            abort(400, "Only one query allowed, 'message'")

        parser = reqparse.RequestParser()
        parser.add_argument(
            "message", type=str, required=True, help="message query is missing."
        )
        args = parser.parse_args()
        response = args

        if message:
            response = args, 200, {"set_message": message}

        return response
