from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.purchase_order import PurchaseOrder
from app.schemas.purchase_order import (
    PurchaseOrderCreate,
    PurchaseOrderResponse
)

router = APIRouter()

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Purchase Order
@router.post(
    "/purchase-orders",
    response_model=PurchaseOrderResponse
)
def create_purchase_order(
    po: PurchaseOrderCreate,
    db: Session = Depends(get_db)
):
    new_po = PurchaseOrder(
        po_number=po.po_number,
        item_name=po.item_name,
        quantity=po.quantity,
        unit_cost=po.unit_cost,
        status=po.status,
        expected_delivery=po.expected_delivery,
        vendor_id=po.vendor_id
    )

    db.add(new_po)
    db.commit()
    db.refresh(new_po)

    return new_po

# Get All Purchase Orders
@router.get(
    "/purchase-orders",
    response_model=list[PurchaseOrderResponse]
)
def get_purchase_orders(
    db: Session = Depends(get_db)
):
    return db.query(PurchaseOrder).all()