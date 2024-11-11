from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship

from .addressModel import AddressModel
from .professionModel import ProfessionModel
from ..config.database import Base


#Model to professionals table
class ProfessionalModel(Base):
    __tablename__ = 'profissionals'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    cpf = Column(String, nullable=False)
    rg = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    id_profession = Column(Integer, ForeignKey('professions.id_profession', ondelete="CASCADE"), nullable=False)
    id_address = Column(Integer, ForeignKey('addresses.id_address', ondelete="CASCADE"), nullable=False)

    address = relationship('AddressModel')
    profession = relationship('ProfessionModel')



#CALLING THE CLASSES TO GET THE FK REFERENCES!
ProfessionModel()
AddressModel()


