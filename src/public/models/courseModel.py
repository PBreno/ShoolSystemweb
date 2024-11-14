from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship

from ..config.database import Base
from ..models.professionalModel import ProfessionalModel
from ..models.subjectsModel import SubjectsModel


#COURSES TABLE MODEL
class CourseModel(Base):
    __tablename__ = 'courses'
    id_course = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    modality = Column(String, nullable=False)
    period = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    id_subject = Column(Integer, ForeignKey('subjects.id_subject'), nullable=False)
    id_professional = Column(Integer, ForeignKey('professionals.id_professional'), nullable=False)

    subject = relationship("SubjectsModel")
    professional = relationship("ProfessionalModel")


#CALLING THE CLASS TO GET THE FK REFERENCES!
SubjectsModel()
ProfessionalModel()