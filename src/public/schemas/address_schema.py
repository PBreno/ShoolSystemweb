from pydantic import BaseModel


class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    uf: str
    zip: str

    class Config:
        from_attributes = True

class AddressCreate(AddressBase):
    pass

class AddressOut(BaseModel):
     id_address: int
     street: str
     city: str
     state: str
     uf: str
     zip: str

     class Config:
         from_attributes = True