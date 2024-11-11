from sqlalchemy import Column, Integer, String

from ..config.database import Base


#PROFESSIONS TABLE MODEL
class ProfessionModel(Base):
    __tablename__ = 'professions'
    id_profession = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)