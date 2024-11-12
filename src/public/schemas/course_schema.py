from datetime import datetime

from pydantic import BaseModel

from ..schemas.professional_schema import Professional


class CouseBase(BaseModel):
    name: str
    duration: int
    modality: str
    period: str
    description: str

    class Config:
        from_attributes = True


class CourseCreate(CouseBase):
    pass


class Course(CourseCreate):
    id: int
    professional: Professional
    created_at: datetime
    class Config:
        from_attributes = True