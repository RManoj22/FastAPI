from sqlalchemy import Column,String,Integer
from database import Base

class Student_Model(Base):
    __tablename__ = "Students"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    age = Column(Integer)