from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...config.database import get_db
from ...controller.courseController import CourseController

router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)

@router.get("/")
async def get_courses(db: Session = Depends(get_db)):
    courses = CourseController.get_all_courses(db)

    return {"courses": courses}