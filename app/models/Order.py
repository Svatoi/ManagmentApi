from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    order_name = Column(String, nullable=False)
    count = Column(Integer, nullable=False)

    deliver = relationship("User", back_populates="orders")
    items = relationship("Item", back_populates="order_item")
