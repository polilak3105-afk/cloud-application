from app.data.services import services_data


def get_all_services():
    return services_data


def get_service_by_id(service_id: int):
    for service in services_data:
        if service["id"] == service_id:
            return service
    return None


def create_service(service):
    services_data.append(service)
    return service


def update_service(service_id: int, updated_service):
    for i, service in enumerate(services_data):
        if service["id"] == service_id:
            services_data[i] = updated_service
            return updated_service
    return None


def delete_service(service_id: int):
    for i, service in enumerate(services_data):
        if service["id"] == service_id:
            return services_data.pop(i)
    return None


def count_services():
    return len(services_data)
# Хранилище данных
services_data = [
    {"service_id": 1, "name": "Cloud Service 1", "status": "active", "description": "Облачный сервис"},
    {"service_id": 2, "name": "Cloud Service 2", "status": "active", "description": "Облачный сервис"},
]

def count_services() -> int:
    """Возвращает количество сервисов в хранилище."""
    return len(services_data)