from app.core.configs import Config


def hello_endpoint(message):

    config = Config()
    msg = config._message

    response = {"message": message}

    if msg:
        response = {"message": message}, 200, {"set_message": msg}

    return response
