from fastapi import APIRouter, Request, HTTPException, Response, Query
from core.config import Config
from core.utils import parse_query_params

router = APIRouter()

router = APIRouter(
    prefix="/hello",
    tags=["hello"],
)


@router.get(
    "",
    responses={
        400: {
            "description": "Bad Request",
            "content": {"application/json": {"example": {"detail": "Error Response"}}},
        },
        200: {
            "description": "Successful Response",
            "content": {"application/json": {"example": {"message": "Query Value"}}},
        },
    },
)
async def hello_endpoint(
    request: Request,
    response: Response,
    message: str = Query(...),
):

    config = Config()
    msg = config._message

    resp = {"message": message}

    if len(parse_query_params(request.query_params)) > 1:
        raise HTTPException(status_code=400, detail="Only one query allowed, 'message'")

    if msg:
        response.headers["set_message"] = msg

    return resp
