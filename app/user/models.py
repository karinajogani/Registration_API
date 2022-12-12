from sqlalchemy.orm import relationship
from db_base.database import Base
from sqlalchemy import String, Integer, Column, DateTime, Boolean
from uuid import UUID
# from app.user.schemas import UserUpdate
# from app.user.routes import user_update, user_to_update

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
    
# class UserUp(User):
#     def userupdate(self, update):
#         self.name = update
#         self.date_of_birth = update
#         self.gender = update
#         self.mail = update
    # user_update = UserUpdate.dict(exclude_unset=True)
    # for key, value in data_to_update.items():
    #     setattr(user_to_update, key, value)
    
# class UserUp(Base):
#     __tablename__ = 'users'
    # def update(self):
    #     user_update = UserUpdate.dict(exclude_unset=True)
    #     for key, value in user_update.items():
    #         setattr(key, value)