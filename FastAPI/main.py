from fastapi import FastAPI, Depends, HTTPException, Path
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db import SessionLocal, Base, engine
from schemas import *
from crud import *

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()