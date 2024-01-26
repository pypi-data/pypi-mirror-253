"""Марштруты для запроса данных и вспомогательных действий"""

from fastapi import APIRouter, Depends, HTTPException

from .utils import make_response
from .auth import oauth2_scheme

from ...core.config import settings
from ...api.schemas.requests import RequestBody
from ...api.schemas.responses import ResponseBody
from ...core.handlers import handlers

router = APIRouter()


@router.get("/")
async def hello():
    return {"message": f'Hello {settings.required.instance}'}


@router.get("/healthcheck")
async def healthckeck():
    return "OK"


@router.post("/api/v1/search", response_model=ResponseBody)
async def get_search_data(request: RequestBody, token=Depends(oauth2_scheme)):
    if token != settings.token:
        return HTTPException(status_code=503, detail="Auth depends")
    # Получаем тип передаваемых данных
    data_type = request.data_type
    # Значения, переданные для поиска
    values: list = request.value
    # Смотрим, есть ли обработчик именно этого класса
    if (search_class := handlers.get(data_type, handlers.get('_all_'))) is not None:
        try:
            # Создание экземляра Вашего класса и передача ему параметров
            searcher = handlers.get_instance(search_class)
            # Передаем результат в функцию подготовки ответа и возвращаем ResponseBody
            success, data = await searcher(data_type, values)
            return make_response(success, data)
        except Exception as error:
            return make_response(False, {"error": error.__str__()})
    else:
        return make_response(False, {"error": "Нет обработчиков для данной операции"})
