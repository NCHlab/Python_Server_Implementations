from flask_restx import Namespace, Resource, fields, reqparse
from flask import request, abort
from app.core.configs import Config
from app.core.utils import parse_data, validate_data

api = Namespace("tests", description="Tests Operation")


resource_fields = api.model(
    "Resource",
    {
        "set_message": fields.String,
    },
)


@api.route("/")
class TestsEndpoint(Resource):
    @api.doc(body=resource_fields)
    def post(self):

        config = Config()

        response = "", 204

        json_data = parse_data(request)
        validate_data(json_data)

        parser = reqparse.RequestParser()
        parser.add_argument(
            "set_message", type=str, required=True, help="message query is missing."
        )
        args = parser.parse_args()

        if not args or len(json_data) > 1:
            abort(400, "Only 'set_message' allowed in body")

        config._message = args["set_message"]

        return response
