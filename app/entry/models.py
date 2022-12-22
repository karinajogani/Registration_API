from pydantic import BaseModel
from db_base.database import Base
from typing import Optional
from sqlalchemy import String, Integer, Column, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.competition.models import Competition

class Entry(Base):
    """create the base class for the database

    Args:
        Base (_type_): _description_
    """
    __tablename__ = 'entries'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(20))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_delete = Column(Boolean, default=False)
    competition_id = Column(UUID, ForeignKey(Competition.id))
