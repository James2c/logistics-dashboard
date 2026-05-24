from sqlalchemy import Column, Integer, String, Float

from app.database import Base

class InventoryItem(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)

    item_name = Column(String, nullable=False, unique=True)

    stock_level = Column(Integer, nullable=False)

    reorder_point = Column(Integer, nullable=False)

    unit_cost = Column(Float, nullable=False)

    location = Column(String)