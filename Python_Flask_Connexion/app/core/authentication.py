def validate_basic_auth(username, password):
    user_info = None

    # Should never hard code user/pass, but this is an example
    if username == "username" and password == "password":
        user_info = {"sub": "user1", "scope": ""}

    return user_info


def validate_bearer_token():
    pass
