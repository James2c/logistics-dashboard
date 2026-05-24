from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.vendor import Vendor

router = APIRouter()

# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Vendor
@router.post("/vendors")
def create_vendor(
    name: str,
    email: str,
    lead_time_days: int,
    reliability_score: float,
    db: Session = Depends(get_db)
):
    vendor = Vendor(
        name=name,
        email=email,
        lead_time_days=lead_time_days,
        reliability_score=reliability_score
    )

    db.add(vendor)
    db.commit()
    db.refresh(vendor)

    return vendor

# Get All Vendors
@router.get("/vendors")
def get_vendors(db: Session = Depends(get_db)):
    vendors = db.query(Vendor).all()
    return vendors