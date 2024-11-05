from typing import Type, Any

from fastapi.openapi.models import Response
from sqlalchemy.orm import Session
from starlette import status

from ..config.database import engine
from ..models.studentModel import StudentModel
from ..models import studentModel
from ..schemas.student_schema import StudentCreate

studentModel.Base.metadata.create_all(bind=engine)

class StudentController:


    @staticmethod
    def get_all_students(db: Session) -> list:

        return db.query(StudentModel).all()


    @staticmethod
    def get_student_by_id(student_id: int, db: Session ) -> Type[StudentModel] | None:

        return db.query(StudentModel).filter(StudentModel.id == student_id).first()


    @staticmethod
    def create_student(student: StudentCreate, db: Session) -> StudentModel:

        new_student = StudentModel(**student.model_dump())
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return new_student


    @staticmethod
    def delete_student(student_id: int, db: Session) ->  None | Response:
        deleted_student = db.query(StudentModel).filter(StudentModel.id == student_id)

        if deleted_student.first() is None:
            return deleted_student.first()

        deleted_student.delete(synchronize_session=False)
        db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)


    @staticmethod
    def update_student(student_id: int, student: StudentCreate, db: Session) -> Type[StudentModel] | None:
        updated_student = db.query(StudentModel).filter(StudentModel.id == student_id)

        if updated_student.first() is None:
            return updated_student.first()

        updated_student.update(student.model_dump())
        db.commit()

        return updated_student.first()