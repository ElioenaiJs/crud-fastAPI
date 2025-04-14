from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from db.db import engine
from datetime import datetime


Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), index=True)         
    description = Column(String(255), index=True)  
    completed = Column(Boolean, default=False)
    due_date = Column(DateTime, nullable=True) 


Base.metadata.create_all(bind=engine)
