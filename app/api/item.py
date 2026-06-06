from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.db_initial import get_db
from app.models.Item import Item
from app.schemas.Item import ItemCreate, ItemOut

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

@router.post("/", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
def create_item(item_in: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(
        item_name=item_in.item_name,
        description=item_in.description,
        type=item_in.type,
        price=item_in.price,
        quantity=item_in.quantity
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=List[ItemOut])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = db.query(Item).offset(skip).limit(limit).all()
    return items
