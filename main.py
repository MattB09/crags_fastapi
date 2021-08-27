from typing import Optional, List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas, crud
from models import Style, Crag, Prefecture, Base
from database import db_session, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return {"docs": "visit docs at /docs"}


@app.post("/styles", response_model=schemas.Style)
def create_style(style: schemas.StyleCreate, db: Session = Depends(get_db)):
    existing_style = crud.get_style_by_name(db, style.name)
    if existing_style:
        raise HTTPException(status_code=400, detail="Style already exists")
    return crud.create_style(db=db, style=style)

@app.get("/styles", response_model=List[schemas.Style])
def read_styles(db: Session = Depends(get_db)):
    styles = crud.get_styles(db)
    return styles

@app.get("/styles/{style_id}", response_model=schemas.Style)
def read_style(style_id: int, db: Session = Depends(get_db)):
    style = crud.get_style(db, style_id)
    if style is None:
        raise HTTPException(status_code=404, detail="Style not found")
    return style

@app.put("/styles/{style_id}", response_model=schemas.Style)
def update_style(style_id: int, style: schemas.StyleCreate, db: Session = Depends(get_db)):
    # verify id is valid
    existing_style = crud.get_style(db, style_id)
    if existing_style is None:
        raise HTTPException(status_code=404, detail="Style not found")

    # verify style.name is not a duplicate
    duplicate_style = crud.get_style_by_name(db, style.name)
    if duplicate_style and duplicate_style.id != style_id:
        raise HTTPException(status_code=400, detail=f"Style with name '{style.name}' already exists.")

    return crud.update_style(db, style_id, style)

@app.delete("/styles/{style_id}", status_code=204)
def delete_style(style_id: int, db: Session = Depends(get_db)):
    style = crud.get_style(db, style_id)
    if style is None:
        raise HTTPException(status_code=404, detail="Style not found")
    crud.delete_style(db, style_id)
    return 204

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

@app.post("/prefectures", response_model=schemas.Prefecture)
def create_prefecture(prefecture: schemas.PrefectureCreate, db: Session = Depends(get_db)):
    existing_prefecture = crud.get_prefecture_by_name(db, prefecture.name)
    if existing_prefecture:
        raise HTTPException(status_code=400, detail="Prefecture already exists")
    return crud.create_prefecture(db, prefecture)

@app.get("/prefectures", response_model=List[schemas.Prefecture])
def read_prefectures(db: Session = Depends(get_db)):
    return crud.get_prefectures(db)

@app.get("/prefectures/{prefecture_id}", response_model=schemas.Prefecture)
def read_prefecture(prefecture_id: int, db: Session = Depends(get_db)):
    prefecture = crud.get_prefecture(db, prefecture_id)
    if prefecture is None:
        raise HTTPException(status_code=404, detail="Prefecture not found")
    return prefecture