import datetime

from typing import List, Optional
from pydantic import BaseModel


class CragBase(BaseModel):
    name: str
    city: Optional[str] = None
    description: Optional[str] = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    style_id: int
    prefecture_id: int

class CragCreate(CragBase):
    pass

class Crag(CragBase):
    id: int

    class Config:
        orm_mode = True
        

class StyleBase(BaseModel):
    name: str
    description: Optional[str] = None

class StyleCreate(StyleBase):
    pass

class Style(StyleBase):
    id: int
    crags: List[Crag] = []

    class Config:
        orm_mode = True


class PrefectureBase(BaseModel):
    name: str

class PrefectureCreate(PrefectureBase):
    pass

class Prefecture(PrefectureBase):
    id: int
    crags: List[Crag] = []

    class Config:
        orm_mode = True