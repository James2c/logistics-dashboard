from fastapi import FastAPI

from app.core.database import Base, engine
from app.models.vendor import Vendor
from app.models.purchase_order import PurchaseOrder
from app.models.inventory import InventoryItem

from app.routes import vendors, purchase_orders, inventory

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Logistics Dashboard API")

app.include_router(vendors.router)
app.include_router(purchase_orders.router)
app.include_router(inventory.router)


@app.get("/")
def root():
    return {"message": "Logistics Dashboard API Running"}