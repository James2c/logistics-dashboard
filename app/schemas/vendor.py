from pydantic import BaseModel, EmailStr

class VendorCreate(BaseModel):
    name: str
    email: EmailStr
    lead_time_days: int
    reliability_score: float

class VendorResponse(VendorCreate):
    id: int

    class Config:
        from_attributes = True