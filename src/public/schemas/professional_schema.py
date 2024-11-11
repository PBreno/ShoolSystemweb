from datetime import date, datetime

from pydantic import BaseModel, EmailStr
from .profession_schema import ProfessionOut, ProfessionBase
from .address_schema import AddressOut


class ProfessionalBase(BaseModel):
    name: str
    email: EmailStr
    birth_date: date
    cpf: str
    rg: str
    phone: str

class ProfessionalCreate(ProfessionalBase):
    pass


class Professional(ProfessionalCreate):
    id: int
    profession: ProfessionOut
    address: AddressOut
    created_at: datetime

    class Config:
        from_attributes = True

class ProfessionalOut(BaseModel):
    professional: Professional

    class Config:
        from_attributes = True
