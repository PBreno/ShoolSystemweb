from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from ...config.database import get_db
from ...controller.professionController import professionController
from ...schemas.profession_schema import ProfessionCreate, ProfessionOut

router = APIRouter(
    prefix="/professions",
    tags=["professions"]
)

@router.get("/")
async def get_professions(db: Session = Depends(get_db)):
    profession = professionController.get_all_professions(db)

    if not profession:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No addresses found")

    return profession


@router.get("/{profession_id}")
async def get_profession_by_id(profession_id: int, db: Session = Depends(get_db)):
    profession = professionController.get_profession_by_id(profession_id, db)

    if not profession:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Profession with ID  {profession_id} not found")

    return profession


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_profession(profession: ProfessionCreate, db: Session = Depends(get_db)):
    profession = professionController.create_profession( db, profession)

    if not profession:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f" The input datas is not correct")

    return profession


@router.delete('/{profession_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_profession(profession_id: int, db: Session = Depends(get_db)):
    _deleted = professionController.delete_profession(profession_id, db)

    if not _deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Profession with ID {profession_id} not found")

    return _deleted


@router.put('/{id_profession}', response_model=ProfessionOut)
async def update_profession(id_profession: int, profession: ProfessionCreate, db: Session = Depends(get_db)):
    profession = professionController.update_profession(id_profession, db, profession)

    if not profession:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Profession with ID {id_profession} not found")

    return profession