from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import Institution
from database import institution_collection

app = FastAPI()

# CORS (Vite frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/institution/register")
def register_institution(data: Institution):
    result = institution_collection.insert_one(data.dict())

    return {
        "status": "success",
        "institution_id": str(result.inserted_id),
        "message": "Institution registered successfully"
    }

