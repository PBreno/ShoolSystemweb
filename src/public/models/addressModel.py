from sqlalchemy import Column, Integer, String

from ..config.database import Base


#ADDRESS TABLE MODEL
class AddressModel(Base):
    __tablename__ = 'addresses'
    id_address = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    uf = Column(String, nullable=False)
    zip = Column(String, nullable=False)


