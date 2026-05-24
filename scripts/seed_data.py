from app.database import SessionLocal, Base, engine
from app.models.vendor import Vendor
from app.models.purchase_order import PurchaseOrder
from app.models.inventory import InventoryItem

import random

# Ensure tables exist
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# -------------------------
# CLEAR EXISTING DATA
# -------------------------
db.query(PurchaseOrder).delete()
db.query(InventoryItem).delete()
db.query(Vendor).delete()

db.commit()

# -------------------------
# VENDORS
# -------------------------
vendors = [
    Vendor(name="ABC Industrial Supply", email="abc@supply.com", lead_time_days=12, reliability_score=92.5),
    Vendor(name="Global Steel Co", email="contact@globalsteel.com", lead_time_days=8, reliability_score=95.2),
    Vendor(name="NorthStar Logistics", email="ops@northstar.com", lead_time_days=15, reliability_score=88.0),
    Vendor(name="Prime Parts Ltd", email="sales@primeparts.com", lead_time_days=6, reliability_score=97.1),
    Vendor(name="Eastern Components", email="info@eastern.com", lead_time_days=10, reliability_score=90.3),
]

db.add_all(vendors)
db.commit()

# Refresh to get IDs
vendors = db.query(Vendor).all()

# -------------------------
# INVENTORY
# -------------------------
inventory_items = [
    InventoryItem(item_name="Steel Bearings", stock_level=120, reorder_point=200, unit_cost=12.5, location="Warehouse A"),
    InventoryItem(item_name="Hydraulic Pumps", stock_level=45, reorder_point=80, unit_cost=250.0, location="Warehouse B"),
    InventoryItem(item_name="Industrial Bolts", stock_level=900, reorder_point=300, unit_cost=0.15, location="Warehouse A"),
    InventoryItem(item_name="Conveyor Belts", stock_level=20, reorder_point=50, unit_cost=500.0, location="Warehouse C"),
    InventoryItem(item_name="Gear Assemblies", stock_level=75, reorder_point=100, unit_cost=120.0, location="Warehouse B"),
    InventoryItem(item_name="Motor Controllers", stock_level=30, reorder_point=60, unit_cost=320.0, location="Warehouse C"),
    InventoryItem(item_name="Aluminum Sheets", stock_level=500, reorder_point=200, unit_cost=8.0, location="Warehouse A"),
]

db.add_all(inventory_items)
db.commit()

# -------------------------
# PURCHASE ORDERS
# -------------------------
statuses = ["Pending", "Ordered", "Shipped", "Delivered"]

purchase_orders = []

for i in range(1, 21):

    vendor = random.choice(vendors)

    po = PurchaseOrder(
        po_number=f"PO-{1000 + i}",
        item_name=random.choice([
            "Steel Bearings",
            "Hydraulic Pumps",
            "Industrial Bolts",
            "Conveyor Belts",
            "Gear Assemblies"
        ]),
        quantity=random.randint(10, 500),
        unit_cost=random.uniform(5, 500),
        status=random.choice(statuses),
        expected_delivery=f"2026-06-{random.randint(1, 28)}",
        vendor_id=vendor.id
    )

    purchase_orders.append(po)

db.add_all(purchase_orders)
db.commit()

print("Dummy data seeded successfully!")