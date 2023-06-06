# The above class defines a Pydantic schema for a student with ID, name, and age attributes, and
# enables ORM mode.
from pydantic import BaseModel

class Student_Schema(BaseModel):
    id : int
    name : str
    age : int

    class Config:
        orm_mode = True
        # media_type = "application/json"