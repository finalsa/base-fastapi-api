from typing import Any
from core.controllers.authorization import login_validate, login, logout
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Form, Request, APIRouter, Depends
from typing import Any
from models import Session

router = APIRouter()


@router.post(
    "/login/",
    response_model=Session
)
async def method_login(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    Creates a new session model to authorize all the requests that the API requires
    """
    username = form_data.username
    password = form_data.password
    ip = request.client.host
    result = await login(ip, username, password)
    return result


@router.post("/logout/{token}/")
async def method_logout(
    *,
    token: str,
    request: Request = {},
):
    """
    Invalidate Session model to unauthorize an access to a computer
    """
    ip = request.client.host
    result = await logout(ip, token)
    return result


@router.post('/login/validate/{token}/')
async def method_login_validate(
    *,
    token: str,
    request: Request = {},
    id: str = Form(...)
):
    """
    Validates the session model and token.
    """
    ip = request.client.host
    result = await login_validate(token, ip, id)
    return result
