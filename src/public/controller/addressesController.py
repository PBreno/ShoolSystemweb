from fastapi import status, Response
from sqlalchemy.orm import Session

from ..models.addressModel import AddressModel
from ..schemas.address_schema import AddressCreate


class AddressController:

    @staticmethod
    def read_addresses(db: Session):
        return db.query(AddressModel).all()

    @staticmethod
    def read_address_by_id(address_id: int, db: Session):
        return db.query(AddressModel).filter(AddressModel.id_address == address_id).first()

    @staticmethod
    def create_address(address: AddressCreate, db: Session):

        address = AddressModel(**address.model_dump())
        db.add(address)
        db.commit()
        db.refresh(address)

        return address

    @staticmethod
    def update_address(address_id: int, address: AddressCreate, db: Session):
        address_updated = db.query(AddressModel).filter(AddressModel.id_address == address_id)

        address_updated.update(address.model_dump())
        db.commit()

        return address_updated.first()

    @staticmethod
    def delete_address(address_id: int , db: Session):
        address_deleted = db.query(AddressModel).filter(AddressModel.id_address == address_id)

        if address_deleted.first() is None:
            return Response(status_code=status.HTTP_404_NOT_FOUND)

        address_deleted.delete(synchronize_session=False)
        db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)
