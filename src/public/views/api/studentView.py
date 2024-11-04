from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from ...config.database import get_db
from ...controller.studentController import StudentController

router = APIRouter(
    tags=["Student"],
    prefix="/students"
)
@router.get('/')
async def get_students(db: Session = Depends(get_db)):

    students = StudentController.get_all_students(db)

    if not students:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No students enrolled')

    return students
