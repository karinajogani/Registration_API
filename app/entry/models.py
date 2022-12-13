from pydantic import BaseModel
from db_base.database import Base
from typing import Optional
from sqlalchemy import String, Integer, Column, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_delete = Column(Boolean, default=False)
    # owner2_id = Column(Integer, ForeignKey("competitions.id"))

    # owner2 = relationship("Competition", back_populates = "entry")
