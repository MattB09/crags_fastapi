from datetime import datetime as dt
from sqlalchemy import select
from sqlalchemy.orm import Session

import schemas
from models import Crag, Style, Prefecture

def create_style(db: Session, style: schemas.StyleCreate):
    new_style = Style(name=style.name, description=style.description)
    db.add(new_style)
    db.commit()
    db.refresh(new_style)
    return new_style

def get_styles(db: Session):
    return db.query(Style).all()

def get_style(db: Session, style_id: int):
    return db.query(Style).get(style_id)

def get_style_by_name(db: Session, name: int):
    return db.query(Style).filter(Style.name == name).first()

def update_style(db: Session, style_id: int, style: schemas.StyleCreate):
    updated_style = db.query(Style).get(style_id)
    updated_style.name = style.name
    updated_style.description = style.description
    db.commit()
    db.refresh(updated_style)
    return updated_style

def delete_style(db: Session, style_id: int):
    deleted_style = db.query(Style).get(style_id)
    db.delete(deleted_style)
    db.commit()


def create_prefecture(db: Session, prefecture: schemas.PrefectureCreate):
    new_pref = Prefecture(name=prefecture.name)
    db.add(new_pref)
    db.commit()
    db.refresh(new_pref)
    return new_pref

def get_prefectures(db: Session):
    return db.query(Prefecture).all()

def get_prefecture(db: Session, prefecture_id: int):
    return db.query(Prefecture).get(prefecture_id)

def get_prefecture_by_name(db: Session, name: str):
    return db.query(Prefecture).filter(Prefecture.name == name).first()

def update_prefecture(db: Session, prefecture_id: int, prefecture: schemas.PrefectureCreate):
    updated_pref = db.query(Prefecture).get(prefecture_id)
    updated_pref.name = prefecture.name
    db.commit()
    db.refresh(updated_pref)
    return updated_pref

def delete_prefecture(db: Session, prefecture_id: int):
    deleted_pref = db.query(Prefecture).get(prefecture_id)
    db.delete(deleted_pref)
    db.commit()


def create_crag(db: Session, crag: schemas.CragCreate):
    new_crag = Crag(
        name=crag.name, 
        city=crag.city,
        description=crag.description,
        style_id=crag.style_id,
        prefecture_id=crag.prefecture_id
    )
    db.add(new_crag)
    db.commit()
    db.refresh(new_crag)
    query = select(
        Crag.id, Crag.name, Crag.city, Crag.description, Crag.created_at, Crag.updated_at, Crag.style_id, Crag.prefecture_id, (Prefecture.name).label("prefecture_name"), (Style.name).label("style_name")
    ).where(Crag.prefecture_id == Prefecture.id).where(Crag.style_id == Style.id).where(Crag.id == new_crag.id)
    return db.execute(query).first()

def get_crags(db: Session):
    query = select(
        Crag.id, Crag.name, Crag.city, Crag.description, Crag.created_at, Crag.updated_at, Crag.style_id, Crag.prefecture_id, (Prefecture.name).label("prefecture_name"), (Style.name).label("style_name")
    ).where(Crag.prefecture_id == Prefecture.id).where(Crag.style_id == Style.id)
    return db.execute(query).all()

def get_crag(db: Session, crag_id: int):
    query = select(
        Crag.id, 
        Crag.name, 
        Crag.city, 
        Crag.description, 
        Crag.created_at, 
        Crag.updated_at, 
        Crag.style_id,
        (Style.name).label("style_name"),
        Crag.prefecture_id, 
        (Prefecture.name).label("prefecture_name"),
    )\
        .where(Crag.prefecture_id == Prefecture.id)\
        .where(Crag.style_id == Style.id)\
        .where(Crag.id == crag_id)
    return db.execute(query).first()

def get_crag_by_name(db: Session, name: str):
    return db.query(Crag).filter(Crag.name == name).first()

def update_crag(db: Session, crag_id: int, crag: schemas.CragCreate):
    pass

def delete_crag(db: Session, crag_id: int):
    deleted_crag = db.query(Crag).get(crag_id)
    db.delete(deleted_crag)
    db.commit()
    