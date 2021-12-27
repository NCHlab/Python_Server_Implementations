from fastapi import APIRouter, Request, HTTPException, status, Depends
from pydantic import BaseModel
from typing import Optional

from core.config import Config
from core.utils import validate_bearer_token

router = APIRouter(
    prefix="/fixes",
    tags=["fixes"],
)


class SetMessage(BaseModel):
    set_message: Optional[str]


@router.put(
    "/id/{num}",
    status_code=status.HTTP_201_CREATED,
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
    num: int,
    request: Request,
    Message: SetMessage,
    credentials: str = Depends(validate_bearer_token),
):

    config = Config()

    if num != 1:
        raise HTTPException(status_code=400, detail="Valid id range: 1-1")

    data = await request.json()
    data_msg = data.get("set_message", None)

    if not data_msg:
        config._message = None
    else:
        config._message = data_msg

    return data
