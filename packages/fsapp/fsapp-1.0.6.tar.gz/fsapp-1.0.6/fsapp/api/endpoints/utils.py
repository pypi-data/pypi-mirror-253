from datetime import datetime
from typing import Union

from ...core.config import settings


def make_response(success_mark: bool, data: Union[dict, str]) -> dict:
    """
    Создание универсального ответа на запросы
    """
    return {
        "instance": settings.required.instance,
        "ts": datetime.now().timestamp(),
        "result": success_mark,
        "data": data
    }
