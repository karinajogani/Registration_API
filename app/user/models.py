from sqlalchemy.orm import relationship
from db_base.database import Base
from sqlalchemy import String, Integer, Column, DateTime, Boolean
from uuid import UUID

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    date_of_birth = Column(DateTime)
    gender = Column(String(10))
    mail = Column(String(50))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_delete = Column(Boolean, default=False)
    # password = Column(String)
    
    competitions = relationship("Competition", back_populates="owner")
    
