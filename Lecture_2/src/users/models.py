from sqlalchemy import Column, Integer, String, Boolean, DateTime
from src.utills.db import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    username = Column(String(150), nullable=False)
    hash_password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)