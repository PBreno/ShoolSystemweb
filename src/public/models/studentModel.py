from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, text
from ..config.database import Base


class StudentModel(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    cpf = Column(String, nullable=False)
    rg = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))