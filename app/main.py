from fastapi import FastAPI

from app.database import engine, Base
from app.models.vendor import Vendor
from app.routes import vendors

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(vendors.router)

@app.get("/")
def root():
    return {"message": "Logistics Dashboard API Running"}