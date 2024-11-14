from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.openapi.utils import status_code_ranges
from sqlalchemy.orm import Session

from ...config.database import get_db
from ...controller.subjectController import SubjectController
from ...schemas.subject_schema import Subject, SubjectCreate

router = APIRouter(
    prefix="/subjects",
    tags=["subjects"],
)

@router.get('/')
async def get_subjects(db: Session = Depends(get_db)):
    subjects = SubjectController.read_subject(db)

    if not subjects:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "No subjects found")

    return subjects


@router.get('/{id}')
async def get_subject(id: int, db: Session = Depends(get_db)):
    subject = SubjectController.read_subject_by_id( id, db)

    if not subject:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= f"Subject with ID {id} not found")

    return subject


@router.post('/')
async def create_subject(subject: SubjectCreate, db: Session = Depends(get_db)):

    subject = SubjectController.create_subject(subject, db)

    if not subject:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= f"Error creating subjects")

    return subject


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_subject(id: int, db: Session = Depends(get_db)):
    subject = SubjectController.delete_subject(id, db)

    if subject is not status.HTTP_204_NO_CONTENT:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= f"Subject with ID {id} not found")

    return subject


@router.put('/{id}')
async def update_subject(id: int, subject: SubjectCreate, db: Session = Depends(get_db)):

    subject = SubjectController.updated_subject(id, subject, db)

    if not subject:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= f"Subject with ID {id} not found")

    return subject


