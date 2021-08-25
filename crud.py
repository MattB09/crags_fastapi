from sqlalchemy.orm import Session

import models, schemas


def get_style(db: Session, style_id: int):
    return db.query(models.Style).filter(models.Style.id == style_id).first()

def get_styles(db: Session):
    return db.query(models.Style).all()
