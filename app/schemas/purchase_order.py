from pydantic import BaseModel

class PurchaseOrderCreate(BaseModel):
    po_number: str
    item_name: str
    quantity: int
    unit_cost: float
    status: str
    expected_delivery: str
    vendor_id: int

class PurchaseOrderResponse(PurchaseOrderCreate):
    id: int

    class Config:
        from_attributes = True