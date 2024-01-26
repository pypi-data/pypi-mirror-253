"""Модели для запросов к API"""

from pydantic import BaseModel
from typing import List


class RequestBody(BaseModel):
    # Модель для проверки запросов к апи
    data_type: str
    value: List
    optional: dict
