from db_base.database import Base
from sqlalchemy import String, Integer, Column


class Userauth(Base):
    __tablename__ = "userauth"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
