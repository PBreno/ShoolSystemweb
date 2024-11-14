from pydantic import BaseModel


class SubjectBase(BaseModel):
    name: str
    credit: int
    workload: int

    class Config:
        from_attributes = True

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectCreate):
    id_subject: int
    name: str
    credit: int
    workload: int


    class Config:
        from_attributes = True