from werkzeug.exceptions import BadRequest, Unauthorized, MethodNotAllowed
from app.routes import api


@api.errorhandler(MethodNotAllowed)
def method_not_allowed_405(err):
    response = {"error": "{}".format(err)}, 405
    return response


@api.errorhandler(BadRequest)
def method_not_allowed_400(err):
    response = {"error": "{}".format(err)}, 400
    return response


@api.errorhandler(Unauthorized)
def method_not_allowed_401(err):
    response = {"error": "{}, bad token, or incorrect Auth Details".format(err)}, 401
    return response
