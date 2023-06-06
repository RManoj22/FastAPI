from fastapi import FastAPI,Query,Path,Body
from enum import Enum
from pydantic import BaseModel,Required,Field

app = FastAPI()

@app.get("/", description="First Route")
async def message():
    return {"msg":"Hello World"}

#path parameters

@app.get("/items/{item_id}")
async def display(item_id:int):
    return {"item_id":item_id}

# using enumerations

class Names(str,Enum):
    John = "John"
    Sam = "Sam"
    Sara = "Sara"

@app.get("/Names/{Your_Name}")
async def list_names(Your_Name:Names):
    if Your_Name == Names.John:
        return {"Hi":Your_Name}
    elif Your_Name.value == "Sam":
        return {"Hi":Your_Name}
    return {"Hi":Names.Sara}

# query parameters

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/db")
async def get_db(skip: int=0, limit:int=10):
    return fake_items_db[skip:skip+limit]

# optional query parameters

@app.get("/msg/{msg}")
async def msg( msg:str, q:int |None=None):
    if q:
        return{"msg":msg,"q":q}
    return{"msg":msg}


# query parameter type conversion

@app.get("/conv/{msg}")
async def type( msg:str,state: bool = False):
    if not state:
        return{"msg":msg,"state":state}
    return{"msg":"msg","state":state}

# request body

class Details(BaseModel):
    name:str
    age:int 
    email: str | None = None

@app.post("/details/{id}")
async def details( details: Details, id:int, q:str |None=None ):
    result = {"id": id, **details.dict()}
    if q:
        result.update({"q": q})
    return result

# query parameters and string validations

@app.get("/valid")
async def valid(q: list[str] | None = Query(["hello","world"], min_length=1, max_length=20) ):
    result = {"q": q}
    return result

# path parameters and numeric validations

@app.get("/path_valid/{id}")
async def pathvalid(id:int = Path(title="id of the path", gt=1), q : str | None = Query(default= None)):
    res = {"id":id}
    if q:
        res.update({"q":q})

    return res


# required query parameter should be before while using path with default 

@app.get("/path_valid_order/{id}")
async def pathvalid_order(q : str, id:int = Path(title="id of the path")):
    res = {"id":id}
    if q:
        res.update({"q":q})

    return res


# to do that without getting errors use * as the first parameter

@app.get("/path_valid_using_*/{id}")
async def pathvalid_trick(*,id:int = Path(title="id of the path"),q : str):
    res = {"id":id}
    if q:
        res.update({"q":q})

    return res


# multiple body parameters and declaring single value as body parameter 
 
class User(BaseModel):
    username: str
    full_name: str | None = None

# add body(embed = True) while having single body but fastapi should expect it as json with key

@app.post("/multiple_body")
async def multiple_body(Name: Names, user: User, importance: int = Body(embed=True)):
    results = {"name": Name, "user": user, "importance": importance}
    return results

# declare example request
 
class User(BaseModel):
    username: str = Field(example = "john")
    full_name: str | None = None
    class config:
        schema_extra = {
            "example":{
                "username" : "john",
                "full_name" : "john doe",
            }
        }
    class Config:
        orm_mode = True
# this helps us in converting our pydantic sqlalchemy models into json