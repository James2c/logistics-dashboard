from fastapi import FastAPI

from app.database import engine, Base

from app.models.vendor import Vendor
from app.models.purchase_order import PurchaseOrder
from app.models.inventory import InventoryItem

from app.routes import vendors
from app.routes import purchase_orders
from app.routes import inventory


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(vendors.router)
app.include_router(purchase_orders.router)
app.include_router(inventory.router)

@app.get("/")
def root():
    return {"message": "Logistics Dashboard API Running"}