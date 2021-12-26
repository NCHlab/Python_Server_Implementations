from flask_restx import Api
from .hello import api as hello_api
from .tests import api as tests_api

api = Api(
    version="1.0",
    title="RestX API",
    description="A simple RestX API",
)

api.add_namespace(hello_api)
api.add_namespace(tests_api)
