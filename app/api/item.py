from typing import List, Optional
from fastapi import APIRouter, Depends, status, Query

from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import ItemCreate, ItemOut
from app.models import Item, User

from .deps import get_current_admin

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

@router.post("/", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
def create_item(item_in: ItemCreate, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
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
def read_items(
    skip: int = 0, 
    limit: int = 10, 
    search: Optional[str] = Query(None, description="Search by product name"),
    item_type: Optional[str] = Query(None, description="Filter by type/category of product"),
    min_price: Optional[float] = Query(None, description="Minimum price"),
    max_price: Optional[float] = Query(None, description="Maximum price"),
    db: Session = Depends(get_db)
    ):

    query = db.query(Item)

    if search:
        query = query.filter(Item.item_name.ilike(f"%{search}%"))

    elif item_type:
        query = query.filter(Item.type == item_type)

    elif min_price is not None:
        query = query.filter(Item.price >= min_price) 

    elif max_price is not None:
        query = query.filter(Item.price <= max_price)

    items = query.offset(skip).limit(limit).all()
    return items
