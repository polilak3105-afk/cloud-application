from pydantic import BaseModel, Field


class ServiceCreate(BaseModel):
    name: str
    type: str
    status: str
