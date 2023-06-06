from fastapi import FastAPI
from database import Base,engine,SessionLocal
from routers import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

db = SessionLocal()

app.include_router(router)

