from fastapi import Depends
from sqlalchemy.orm import Session

from ..models import studentModel
from ..config.database import get_db
from ..models.studentModel import StudentModel


class StudentController:
    @staticmethod
    def get_all_students(db: Session) -> list:

        students =db.query(StudentModel).all()

        return students