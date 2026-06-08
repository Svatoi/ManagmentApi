from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User, Item, Order
from app.schemas import OrderCreate, OrderOut

from .deps import get_current_user

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/", response_model=OrderOut, status_code=status.HTTP_201_CREATED)
def create_order(order_in: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
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
        user_id=current_user.id
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order