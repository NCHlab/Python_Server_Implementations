import os
import base64
from dotenv import load_dotenv

from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer

load_dotenv()

security_basic_auth = HTTPBasic()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def parse_query_params(query):
    query = str(query)
    query_list = query.split("&")

    return query_list


def validate_basic_auth(
    credentials: HTTPBasicCredentials = Depends(security_basic_auth),
):

    auth_from_user = base64.b64encode(
        bytes("{}:{}".format(credentials.username, credentials.password), "utf-8")
    ).decode("utf-8")

    auth_from_user = "Basic " + auth_from_user
    auth = os.environ.get("BASIC_AUTHENTICATION")

    if auth_from_user != auth:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized. You do not have the correct credentials.",
            headers={"WWW-Authenticate": "Basic"},
        )


def validate_bearer_token(token: str = Depends(oauth2_scheme)):

    auth = os.environ.get("OAUTH_AUTHENTICATION")

    if token != auth[7:]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized. You do not have the correct Token Auth.",
            headers={"WWW-Authenticate": "Bearer"},
        )
