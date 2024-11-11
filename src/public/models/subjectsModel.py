from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .professionalModel import ProfessionalModel
from ..config.database import Base


#SUBJECTS TABLE MODEL
class SubjectsModel(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)
    workload = Column(String, nullable=False)
    id_professional = Column(String, ForeignKey('professionals.id', ondelete="CASCADE"), nullable=False)

    professional = relationship('Professionals')

#CALLING THE CLASS TO GET THE FK REFERENCES!
ProfessionalModel()