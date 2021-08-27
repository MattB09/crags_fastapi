from sqlalchemy.orm import Session

import models, schemas


def create_style(db: Session, style: schemas.StyleCreate):
    new_style = models.Style(name=style.name, description=style.description)
    db.add(new_style)
    db.commit()
    db.refresh(new_style)
    return new_style

def get_styles(db: Session):
    return db.query(models.Style).all()

def get_style(db: Session, style_id: int):
    return db.query(models.Style).get(style_id)

def get_style_by_name(db: Session, name: int):
    return db.query(models.Style).filter(models.Style.name == name).first()

def update_style(db: Session, style_id: int, style: schemas.StyleCreate):
    updated_style = db.query(models.Style).get(style_id)
    updated_style.name = style.name
    updated_style.description = style.description
    db.commit()
    db.refresh(updated_style)
    return updated_style

def delete_style(db: Session, style_id: int):
    deleted_style = db.query(models.Style).get(style_id)
    db.delete(deleted_style)
    db.commit()
