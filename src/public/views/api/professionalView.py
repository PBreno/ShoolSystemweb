from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from ...config.database import get_db
from ...controller.professionalController import ProfessionalController
from ...models.addressModel import AddressModel
from ...models.professionModel import ProfessionModel
from ...schemas.professional_schema import ProfessionalCreate, ProfessionalOut, Professional

router = APIRouter(
    tags=["Professional"],
    prefix="/professionals"
)
@router.get('/', response_model=List[Professional])
async def get_professionals(db: Session = Depends(get_db)):

    professionals = ProfessionalController.get_all_professionals(db)

    if not professionals:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No professionals enrolled')
    print(professionals)
    return professionals


@router.get('/{id}',  response_model=Professional)
async def get_professional(id: int, db: Session = Depends(get_db)):
    professional = ProfessionalController.get_professional_by_id(id, db)

    if not professional:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'professional with ID {id}, not found')

    return professional


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_professional(professional: ProfessionalCreate,  id_profession: int = ProfessionModel.id_profession, id_address: int = AddressModel.id_address,db: Session = Depends(get_db)):
    print('==================================')
    print('->', id_profession)
    print('->', id_address)
    print('==================================')
    new_professional = ProfessionalController.create_professional(professional,id_profession,id_address, db)


    return new_professional


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_professional(id: int, db: Session = Depends(get_db)):
    professional = ProfessionalController.delete_professional(id, db)

    if not professional:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'professional with ID {id}, not found')

    return professional


@router.put('/{id}')
async def update_professional(id: int, professional: ProfessionalCreate, db: Session = Depends(get_db)):
    professional = ProfessionalController.update_professional(id, professional, db)

    if not professional:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'professional with ID {id}, not found')

    return professional

