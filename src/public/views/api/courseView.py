from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from starlette.responses import Response

from ...config.database import get_db
from ...controller.courseController import CourseController
from ...schemas.course_schema import CourseCreate

router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)

@router.get("/")
async def get_courses(db: Session = Depends(get_db)):
    courses = CourseController.get_all_courses(db)

    return  courses


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CourseCreate)
async def create_course(course: CourseCreate, db: Session = Depends(get_db)):

    course = CourseController.create_course(course, db)

    if not course:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Error creating course")

    return course


@router.get("/{course_id}")
async def get_course_by_id(course_id: int, db: Session = Depends(get_db)):
    course = CourseController.get_course_by_id(course_id, db)

    if not course:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Course with ID {course_id} not found")

    return course


@router.delete("/{course_id}")
async def delete_course_by_id(course_id: int, db: Session = Depends(get_db)):
    course = CourseController.delete_course(course_id, db)
    if not course:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Course with ID {course_id} not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{course_id}")
async def update_course(id: int, course: CourseCreate, db: Session = Depends(get_db)):
    course = CourseController.update_course(id, course, db)

    if not course:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Course with ID {id} not found")

    return course