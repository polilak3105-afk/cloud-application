from fastapi import APIRouter
from app.services.services import count_services

router = APIRouter(
    tags=["System"]
)


@router.get(
    "/status",
    summary="Проверить состояние приложения"
)
def status():
    return {
        "status": "ok"
    }


@router.get(
    "/about",
    summary="Информация о проекте"
)
def about():
    return {
        "application": "Cloud Application",
        "version": "1.0.0",
        "description": "Облачное приложение"
    }


@router.get(
    "/service-count",
    summary="Получить количество сервисов"
)
def service_count():
    return {
        "services": count_services()
    }