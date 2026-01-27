from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = MongoClient("mongodb://localhost:27017")
db = client["edu_registration"]

@app.post("/institution/register")
def register_institution(data: dict):
    db.institutions.insert_one(data)
    return {"message": "Institution registered successfully"}
