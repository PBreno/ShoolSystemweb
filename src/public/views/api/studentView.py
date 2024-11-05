from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from ...config.database import get_db
from ...controller.studentController import StudentController
from ...schemas.student_schema import StudentCreate

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


@router.get('/{id}')
async def get_student(id: int, db: Session = Depends(get_db)):
    student = StudentController.get_student_by_id(id, db)

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Student with ID {id}, not found')

    return student


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = StudentController.create_student(student, db)

    print(new_student)
    return new_student


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(id: int, db: Session = Depends(get_db)):
    student = StudentController.get_student_by_id(id, db)

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Student with ID {id}, not found')

    return student

@router.put('/{id}')
async def update_student(id: int, student: StudentCreate, db: Session = Depends(get_db)):
    student = StudentController.update_student(id, student, db)

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Student with ID {id}, not found')

    return student