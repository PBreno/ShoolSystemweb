from fastapi.openapi.models import Schema
from pydantic import BaseModel


class ProfessionBase(BaseModel):
    name: str


class ProfessionCreate(ProfessionBase):
    pass


class ProfessionOut(BaseModel):
     id_profession: int
     name: str