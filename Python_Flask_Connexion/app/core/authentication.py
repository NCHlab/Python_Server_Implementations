import os
import base64


def validate_basic_auth(username, password):
    user_info = None

    auth_from_user = base64.b64encode(
        bytes("{}:{}".format(username, password), "utf-8")
    ).decode("utf-8")

    auth_from_user = "Basic " + auth_from_user
    auth = os.environ.get("BASIC_AUTHENTICATION")

    if auth_from_user == auth:
        user_info = {"sub": "user1", "scope": ""}

    return user_info


def validate_bearer_token(auth_token):
    user_info = None
    auth = os.environ.get("OAUTH_AUTHENTICATION")

    if auth_token == auth[7:]:
        user_info = {"sub": "user1", "scope": ""}

    return user_info
