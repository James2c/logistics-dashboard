from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id = Column(Integer, primary_key=True, index=True)

    po_number = Column(String, unique=True, nullable=False)
    item_name = Column(String, nullable=False)

    quantity = Column(Integer, nullable=False)
    unit_cost = Column(Float, nullable=False)

    status = Column(String, default="Pending")

    expected_delivery = Column(String)

    vendor_id = Column(Integer, ForeignKey("vendors.id"))

    vendor = relationship("Vendor", back_populates="purchase_orders")