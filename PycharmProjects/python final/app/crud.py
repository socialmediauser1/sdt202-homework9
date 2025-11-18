from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from . import models
from .schemas import ClothingCreate

def list_clothes(session: Session) -> List[models.Clothing]:
    stmt = select(models.Clothing).order_by(models.Clothing.created_at.desc())
    return list(session.scalars(stmt))

def get_clothing(session: Session, clothing_id: int) -> Optional[models.Clothing]:
    return session.get(models.Clothing, clothing_id)

def create_clothing(session: Session, payload: ClothingCreate) -> models.Clothing:
    clothing = models.Clothing(**payload.model_dump())
    session.add(clothing)
    session.commit()
    session.refresh(clothing)
    return clothing

def update_clothing(
    session: Session, clothing: models.Clothing, payload: ClothingCreate
) -> models.Clothing:
    for field, value in payload.model_dump().items():
        setattr(clothing, field, value)
    session.add(clothing)
    session.commit()
    session.refresh(clothing)
    return clothing

def delete_clothing(session: Session, clothing: models.Clothing) -> None:
    session.delete(clothing)
    session.commit()