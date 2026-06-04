from pydantic import BaseModel, Field
from datetime import datetime

class OrderCreate(BaseModel):
    item_id: int
    quantity: int = Field(..., gt=0, description="The quantity in the order must be greater than 0")

class OrderOut(BaseModel):
    id: int
    item_id: int
    user_id: int
    quantity: int
    created_at: datetime

    class Config:
        from_attributes = True

