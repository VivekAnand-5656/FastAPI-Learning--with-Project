from sqlalchemy import Column,Integer,String, Boolean
from src.utills.db import Base

class TaskManager(Base):
    __tablename__ ="tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(500))
    is_completed = Column(Boolean,default=False)