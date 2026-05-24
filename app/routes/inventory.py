from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.inventory import InventoryItem

from app.schemas.inventory import (
    InventoryCreate,
    InventoryResponse
)

router = APIRouter()

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Inventory Item
@router.post(
    "/inventory",
    response_model=InventoryResponse
)
def create_inventory_item(
    item: InventoryCreate,
    db: Session = Depends(get_db)
):
    new_item = InventoryItem(
        item_name=item.item_name,
        stock_level=item.stock_level,
        reorder_point=item.reorder_point,
        unit_cost=item.unit_cost,
        location=item.location
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    stock_status = (
        "LOW STOCK"
        if new_item.stock_level <= new_item.reorder_point
        else "OK"
    )

    return {
        **new_item.__dict__,
        "stock_status": stock_status
    }

# Get All Inventory
@router.get(
    "/inventory",
    response_model=list[InventoryResponse]
)
def get_inventory(
    db: Session = Depends(get_db)
):
    inventory = db.query(InventoryItem).all()

    response = []

    for item in inventory:

        stock_status = (
            "LOW STOCK"
            if item.stock_level <= item.reorder_point
            else "OK"
        )

        response.append({
            **item.__dict__,
            "stock_status": stock_status
        })

    return response