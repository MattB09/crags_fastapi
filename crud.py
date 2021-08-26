from sqlalchemy.orm import Session

import models, schemas


def get_style(db: Session, style_id: int):
    return db.query(models.Style).filter(models.Style.id == style_id).first()

def get_style_by_name(db: Session, name: int):
    return db.query(models.Style).filter(models.Style.name == name).first()

def get_styles(db: Session):
    return db.query(models.Style).all()

def create_style(db: Session, style: schemas.StyleCreate):
    new_style = models.Style(name=style.name, description=style.description)
    db.add(new_style)
    db.commit()
    db.refresh(new_style)
    return new_style

def delete_style(db: Session, style_id: int):
    db.query(models.Style).filter(models.Style.id == style_id).delete()
    db.commit()
    