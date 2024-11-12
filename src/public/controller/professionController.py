from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import Response

from ..models.professionModel import ProfessionModel
from ..schemas.profession_schema import ProfessionCreate


class professionController:

    @staticmethod
    def get_all_professions(db: Session):
       return db.query(ProfessionModel).all()

    @staticmethod
    def get_profession_by_id(id: int, db: Session):
        return db.query(ProfessionModel).filter_by(id_profession=id).first()


    @staticmethod
    def create_profession(db: Session, profession: ProfessionCreate):
        new_profession = ProfessionModel(**profession.model_dump())

        db.add(new_profession)
        db.commit()
        db.refresh(new_profession)
        return new_profession


    @staticmethod
    def delete_profession(id: int, db: Session):
        delete_profession = db.query(ProfessionModel).filter_by(id_profession=id).first()

        #delete_profession.delete(synchronize_session=False)
        db.delete(delete_profession)
        db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)


    @staticmethod
    def update_profession(id_profession: int, db: Session, profession: ProfessionCreate):

        update_profession = db.query(ProfessionModel).filter_by(id_profession=id_profession)

        update_profession.update(profession.model_dump())

        db.commit()

        return update_profession.first()