from app.core.configs import Config


def tests_endpoint(body):

    config = Config()
    msg = config._message

    response = "", 204

    # As a result of connexion handling some bad params, can assume set_message is in body

    if len(body) > 1:
        response = {"error": "Only 'set_message' allowed in body"}, 400
        return response

    config._message = body["set_message"]

    return response
