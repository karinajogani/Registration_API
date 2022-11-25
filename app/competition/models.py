from db_base.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer, Column, DateTime, Boolean, ForeignKey
# from app.entry.models import Entrypy

class Competition(Base):
    __tablename__ = 'competitions'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_delete = Column(Boolean, default=False)
    url = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="competitions")

    # entries = relationship("Entry", back_populates = "owner2")