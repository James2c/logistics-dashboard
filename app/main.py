from fastapi import FastAPI

from app.database import engine, Base
from app.models.vendor import Vendor

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Logistics Dashboard API Running"}