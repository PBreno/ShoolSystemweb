from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from starlette import status

from ...config.database import get_db
from ...schemas.address_schema import AddressBase, AddressOut, AddressCreate
from ...controller.addressesController import AddressController

router = APIRouter(
    prefix="/addresses",
    tags=["address"]
)

@router.get("/", response_model=List[AddressOut])
async def get_addresses(db: Session = Depends(get_db)):
    addresses = AddressController.read_addresses(db)

    if not addresses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No addresses found")

    return addresses


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    address = AddressController.create_address(address, db)

    return address


@router.get("/{id}", response_model=AddressOut)
async def get_address(id: int, db: Session = Depends(get_db)):
    address = AddressController.read_address_by_id(id, db)
    if not address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with ID {id} not found")

    return address


@router.put("/{id}", response_model=AddressOut)
async def update_address(id: int, address: AddressCreate, db: Session = Depends(get_db)):
    address = AddressController.update_address(id, address, db)
    if not address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with ID {id} not found")

    return address


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_address(id: int, db: Session = Depends(get_db)):
    address_delete = AddressController.delete_address(id, db)

    print('-> ',address_delete.status_code)
    if address_delete.status_code is not status.HTTP_204_NO_CONTENT:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                               detail=f"Address with ID {id} not found")

    return address_delete



