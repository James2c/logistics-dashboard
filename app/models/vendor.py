from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    lead_time_days = Column(Integer)
    reliability_score = Column(Float)