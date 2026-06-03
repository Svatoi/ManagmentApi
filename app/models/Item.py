from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    order_item = relationship("Order", back_populates="items")

