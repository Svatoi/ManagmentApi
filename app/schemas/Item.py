from pydantic import BaseModel, Field
from typing import Optional

class ItemBase(BaseModel):
    item_name: str = Field(..., max_length=100)
    description: Optional[str] = None
    type: str = Field(..., max_length=50)
    price: float = Field(..., gt=0, description="The price must be at more 0")
    quantity: int = Field(..., ge=0, description="The quantity in the order must be greater than 0")

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None

class ItemOut(ItemBase):
    id: int

    class Config:
        from_attributes = True

