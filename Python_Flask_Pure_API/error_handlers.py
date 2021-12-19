import flask

blueprint = flask.Blueprint("error_handlers", __name__)


@blueprint.app_errorhandler(405)
def method_not_allowed_405(err):
    response = {"error": "{}".format(err)}, 405
    return response


@blueprint.app_errorhandler(400)
def method_not_allowed_400(err):
    response = {"error": "{}".format(err)}, 400
    return response


@blueprint.app_errorhandler(401)
def method_not_allowed_401(err):
    response = {"error": "{}".format(err)}, 401
    return response
