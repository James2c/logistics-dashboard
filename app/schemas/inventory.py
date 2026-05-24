from pydantic import BaseModel

class InventoryCreate(BaseModel):
    item_name: str
    stock_level: int
    reorder_point: int
    unit_cost: float
    location: str

class InventoryResponse(InventoryCreate):
    id: int
    stock_status: str

    class Config:
        from_attributes = True