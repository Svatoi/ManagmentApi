from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.db_initial import get_db
from app.models.Order import Order
from app.models.Item import Item
from app.schemas.Order import OrderCreate, OrderOut

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/", response_model=OrderOut, status_code=status.HTTP_201_CREATED)
def create_order(order_in: OrderCreate, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == order_in.item_id).first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with that ID not found"
        )
    
    if item.quantity < order_in.quantity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Not enough stock available. Available: {item.quantity} pcs."
        )
    
    item.quantity -= order_in.quantity

    db_order = Order(
        count=order_in.quantity,
        item_id=order_in.item_id,
        user_id=1
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order