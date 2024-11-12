from typing import Type, Any
from sqlalchemy.orm import Session

from ..config.database import engine, Base
from ..models.addressModel import AddressModel
from ..models.courseModel import CourseModel
from ..models.professionalModel import ProfessionalModel
#from ..models import professionalModel
from ..schemas.professional_schema import ProfessionalCreate

Base.metadata.create_all(bind=engine)
#professionalModel.Base.metadata.create_all(bind=engine)

class ProfessionalController:


    @staticmethod
    def get_all_professionals(db: Session):

        professional = (db.query(ProfessionalModel ).
                        join(AddressModel, AddressModel.id_address == ProfessionalModel.id_address, isouter=True).all())

        print(professional)
        return professional


    @staticmethod
    def get_professional_by_id(professional_id: int, db: Session ) -> Type[ProfessionalModel] | None:

        return db.query(ProfessionalModel).filter(ProfessionalModel.id == professional_id).first()


    @staticmethod
    def create_professional(professional: ProfessionalCreate, id_profession: int, id_address: int, db: Session) -> ProfessionalModel:

        new_professional = ProfessionalModel(id_professional=id_profession, id_address=id_address, **professional.model_dump())
        db.add(new_professional)
        db.commit()
        db.refresh(new_professional)
        return new_professional


    @staticmethod
    def delete_professional(professional_id: int, db: Session) ->  None | dict[str, Any]:
        deleted_professional = db.query(ProfessionalModel).filter(ProfessionalModel.id == professional_id)

        #print(deleted_professional.first())
        if deleted_professional.first() is None:
            return deleted_professional.first()

        print('Awq ->', deleted_professional.first())

        deleted_professional.delete(synchronize_session=False)
        #db.delete(deleted_professional.first())
        db.commit()

        return {"professional_id": f" professional with ID {professional_id} deleted!"}


    @staticmethod
    def update_professional(professional_id: int, professional: ProfessionalCreate, db: Session) -> Type[ProfessionalModel] | None:
        updated_professional = db.query(ProfessionalModel).filter(ProfessionalModel.id == professional_id)

        if updated_professional.first() is None:
            return updated_professional.first()

        updated_professional.update(professional.model_dump())
        db.commit()

        return updated_professional.first()