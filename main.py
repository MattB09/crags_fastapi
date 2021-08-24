# from typing import Optional
from fastapi import FastAPI

from models import Style
from database import Base, SessionLocal,engine

Base.metadata.create_all(engine)
session = SessionLocal()

app = FastAPI()


@app.get("/")
def index():
    styles = session.query(Style).all()
    return styles


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}