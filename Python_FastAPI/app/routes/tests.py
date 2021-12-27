from fastapi import APIRouter, Request, HTTPException, Response, status, Depends
from pydantic import BaseModel

from core.config import Config
from core.utils import validate_basic_auth

router = APIRouter(
    prefix="/tests",
    tags=["tests"],
)


class SetMessage(BaseModel):
    set_message: str


@router.post(
    "",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        400: {
            "description": "Bad Request",
            "content": {"application/json": {"example": {"detail": "Error Response"}}},
        },
        200: {
            "description": "Successful Response",
            "content": {"application/json": {"example": {"set_message": "Value"}}},
        },
    },
)
async def tests_endpoint(
    request: Request,
    response: Response,
    Message: SetMessage,
    credentials: str = Depends(validate_basic_auth),
):

    config = Config()
    data = await request.json()

    if len(data) > 1:
        raise HTTPException(
            status_code=400, detail="Only 'set_message' allowed in body"
        )

    config._message = Message.set_message

    return Response(status_code=status.HTTP_204_NO_CONTENT)
