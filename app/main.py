from fastapi import FastAPI
from pydantic import BaseModel

from app.config import APP_NAME, APP_VERSION
from app.routers.services import router as services_router
from app.routers.system import router as system_router

# Метаданные для документации OpenAPI
tags_metadata = [
    {
        "name": "Services",
        "description": "Операции управления программными сервисами Cloud Application.",
    },
    {
        "name": "System",
        "description": "Системные маршруты и метрики.",
    },
]

# Инициализация приложения FastAPI (строго один раз)
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Учебное серверное приложение для изучения разработки ПО облачных систем.",
    openapi_tags=tags_metadata,
)

# Подключение роутеров из соответствующих модулей
app.include_router(system_router)
app.include_router(services_router)


# Главные эндпоинты приложения
@app.get("/", tags=["Main"], summary="Главная страница")
def root():
    return {"message": "Cloud Application работает"}


@app.get(
    "/course",
    tags=["Course"],
    summary="Информация о лабораторной работе",
)
def course():
    return {
        "discipline": "Управление работами и разработка ПО облачных систем",
        "laboratory": 2,
        "project": "Cloud Application",
    }