"""Модели для респонсов от API"""

from pydantic import BaseModel, Field
from typing import Any


class ResponseBody(BaseModel):
    instance: str = Field(title="Instance", description="Сервис, предоставляющий информацию")
    ts: int = Field(title="Timestamp", description="UNIX time выполнения запроса")
    result: bool = Field(title="ResultFlag", description="Результат получен или нет")
    data: Any = Field(title="Data", description="Результат выполнения запроса в общем формате")
