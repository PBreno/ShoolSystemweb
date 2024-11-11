from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.public.models.professionalModel import ProfessionalModel
from src.public.models.subjectsModel import SubjectsModel


#COURSES TABLE MODEL
class CourseModel:
    __tablename__ = 'courses'
    id_course = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    modality = Column(String, nullable=False)
    period = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    id_subject = Column(Integer, ForeignKey('subjects.id_subject'), nullable=False)
    id_professional = Column(Integer, ForeignKey('professionals.id_professional'), nullable=False)

    subject = relationship("SubjectModel")
    professional = relationship("ProfessionalModel")


#CALLING THE CLASS TO GET THE FK REFERENCES!
SubjectsModel()
ProfessionalModel()