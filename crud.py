from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from schemas import Student_Schema
from models import Student_Model

# from database import SessionLocal

# Session = SessionLocal()

def get_student(db:Session):
    return db.query(Student_Model).all()


def get_student_by_id(db:Session, id:int):
    return db.query(Student_Model).filter(Student_Model.id==id).first()


def student_exists(db:Session, request:Student_Schema):
    return db.query(Student_Model).filter(Student_Model.id==request.id).first()


def create_student(db:Session, request:Student_Schema):
    new_info = Student_Model(**request.dict())
    db.add(new_info)
    db.commit()
    return new_info.id


def update_student(db:Session,request:Student_Schema):
    item_update = db.query(Student_Model).filter(Student_Model.id == request.id).first()
    item_update.id = request.id 
    item_update.name = request.name
    item_update.age = request.age
    db.commit()
    return item_update.id


def delete_student(db:Session, id:int):
    item_delete = db.query(Student_Model).filter(Student_Model.id == id).first()
    db.delete(item_delete)
    db.commit()
    return item_delete.id