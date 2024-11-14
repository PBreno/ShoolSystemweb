from datetime import datetime

from pydantic import BaseModel

from ..schemas.professional_schema import Professional


class CourseBase(BaseModel):
    name: str
    duration: int
    modality: str
    period: str
    description: str
    id_subject: int
    id_professional: int

    class Config:
        from_attributes = True


class CourseCreate(CourseBase):
    pass


class Course(CourseCreate):
    id: int
    professional: Professional
    created_at: datetime
    class Config:
        from_attributes = True