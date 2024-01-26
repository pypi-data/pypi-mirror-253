from fastapi import FastAPI

from fsapp.core.config import settings
from fsapp.api.routers import api_router
from fsapp.classes import BaseExecutor
from fsapp.core.config import create_settings_files
from .logger import logger

create_settings_files()

# Основной объект приложения
# todo argument comments
app = FastAPI(
    title=settings.required.instance,
    docs_url="/docs",
    debug=False
)


@app.on_event("startup")
async def on_startup():
    await logger.acritical("Graceful startup", service=app.title)


@app.on_event("shutdown")
async def on_shutdown():
    await logger.acritical("Graceful shutdown", service=app.title)


settings.token = None
# Подключение всех эндпоинтов
app.include_router(api_router)
# Добавляем базовый класс обработчиков
app.base_class = BaseExecutor
