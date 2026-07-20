from fastapi import FastAPI

from database.connection import engine, Base
from database.models import User

app = FastAPI()

print(Base.metadata.tables.keys())
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "Veritas Backend Running"
    }