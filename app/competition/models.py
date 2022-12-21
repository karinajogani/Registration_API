from db_base.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column, DateTime, Boolean, ForeignKey
from app.user.models import User
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Competition(Base):
    __tablename__ = 'competitions'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String(20))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_delete = Column(Boolean, default=False)
    url = Column(String)
    user_id = Column(UUID, ForeignKey(User.id))
