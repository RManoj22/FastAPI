from fastapi import APIRouter,status,HTTPException,Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import Student_Schema
from typing import List
from crud import *

router = APIRouter()

@router.get('/students',response_model=List[Student_Schema],status_code=status.HTTP_200_OK)
def get_student_data(db : Session=Depends(get_db)):
    return get_student(db=db)

@router.get('/students/{id}',response_model=Student_Schema,status_code=status.HTTP_200_OK)
def get_student_data_by_id(id:int,db:Session=Depends(get_db)):
    deed = get_student_by_id(db=db, id=id)
    if deed is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'student with id {id} not found')
    return deed

@router.post('/create_students',status_code=status.HTTP_201_CREATED)
def student_data_created(request:Student_Schema,db:Session=Depends(get_db)):
    deed = student_exists(db=db, request=request)
    if deed:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='id already exists')
    return create_student(db=db, request=request)

@router.put('/update_students',status_code=status.HTTP_200_OK)
def update_student_data(request:Student_Schema,db:Session=Depends(get_db)):
    item_update = update_student(db=db, request= request)
    if not item_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'student with id {id} not found')
    return item_update

@router.delete('/delete_students/{id}',status_code=status.HTTP_200_OK)
def delete_student_data(id:int,db:Session=Depends(get_db)):
    item_delete = delete_student(db=db, id=id)
    if item_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return f'item deleted with id {id}'