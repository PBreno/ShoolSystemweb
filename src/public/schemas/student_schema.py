from datetime import date

from pydantic import BaseModel, EmailStr


class StudentBase(BaseModel):
    name: str
    email: EmailStr
    birth_date: date
    cpf: str
    rg: str
    phone: str

class StudentCreate(StudentBase):
    pass