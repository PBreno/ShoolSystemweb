from fastapi.openapi.models import Response
from sqlalchemy.orm import Session
from starlette import status

from ..models.subjectsModel import SubjectsModel
from ..schemas.subject_schema import SubjectCreate


class SubjectController:

    @staticmethod
    def read_subject(db: Session):
        return db.query(SubjectsModel).all()


    @staticmethod
    def read_subject_by_id( subject_id: int, db: Session):

        subject = db.query(SubjectsModel).filter_by(id_subject=subject_id).first()

        return subject


    @staticmethod
    def create_subject (subject: SubjectCreate, db: Session):

        new_subject = SubjectsModel(**subject.model_dump())

        db.add(new_subject)
        db.commit()
        db.refresh(new_subject)

        return new_subject


    @staticmethod
    def delete_subject(subject_id: int, db: Session):

        delete_subject = db.query(SubjectsModel).filter(SubjectsModel.id_subject == subject_id)

        if delete_subject.first() is None:
            return Response(status_code=status.HTTP_404_NOT_FOUND)

        delete_subject.delete(synchronize_session=False)
        db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)


    @staticmethod
    def updated_subject(subject_id: int, subject: SubjectCreate, db: Session):

        subject_ = db.query(SubjectsModel).filter(SubjectsModel.id_subject == subject_id)

        subject_.update(subject.model_dump())
        db.commit()

        return subject_.first()
