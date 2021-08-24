import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Style(Base):
    __tablename__ = "styles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)

    crags = relationship("Crag", back_populates="style")

class Prefecture(Base):
    __tablename__ = "prefectures"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    crags = relationship("Crag", back_populates="prefecture")

class Crag(Base):
    __tablename__ = "crags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    city = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    style_id = Column(Integer, ForeignKey("styles.id"))
    prefecture_id = Column(Integer, ForeignKey("prefectures.id"))

    style = relationship("Style", back_populates="crags")
    prefecture = relationship("Prefecture", back_populates="crags")