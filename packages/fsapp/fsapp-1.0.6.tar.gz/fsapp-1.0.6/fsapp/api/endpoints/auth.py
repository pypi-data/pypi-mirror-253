"""Маршрут аутентификации и выдаычи токена"""

from hashlib import md5

from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime
from fsapp.core.config import settings

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def get_token():
    token = md5(datetime.now().__str__().encode('utf-8')).hexdigest()
    settings.token = token
    return token


@router.post("/auth/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_name = form_data.username
    password = form_data.password
    if user_name != settings.auth.username:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if md5(password.encode('utf-8')).hexdigest() != settings.auth.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": get_token(), "token_type": "bearer"}


@router.get("/secutiry_test")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    if token == settings.token:
        return {"security": True}
    else:
        return HTTPException(status_code=503, detail="Incorrect token")
