from typing import Optional, List


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas, crud
from models import Style, Crag, Prefecture, Base
from database import Session, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.get("/styles", response_model=List[schemas.Style])
def read_styles(db: Session=Depends(get_db)):
    styles = crud.get_styles(db)
    return styles

@app.get("/styles/{style_id}", response_model = schemas.Style)
def read_style(style_id: int, db: Session=Depends(get_db)):
    style = crud.get_style(db, style_id=style_id)
    if style is None:
        raise HTTPException(status_code=404, detail="Style not found")
    return style

@app.get("/")
def index():
    return {"hello": "world"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}