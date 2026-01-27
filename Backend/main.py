from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

from database import (
    institution_basic_col,
    institution_contact_col,
    institution_address_col,
    institution_academic_col,
    institution_digital_col,
)

app = FastAPI(title="Institution Registration API (Testing Mode)")

# -------------------- CORS --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- ROOT --------------------
@app.get("/")
def root():
    return {"status": "Backend running successfully 🚀"}

# =========================================================
# 1️⃣ BASIC INSTITUTION DETAILS
# =========================================================
@app.post("/institution/basic")
def save_basic_institution(data: Dict):
    """
    Stores:
    - institution name
    - type
    - year
    - NAAC
    - official email
    """
    result = institution_basic_col.insert_one(data)
    return {
        "status": "success",
        "institution_id": str(result.inserted_id),
        "message": "Basic institution data saved"
    }

# =========================================================
# 2️⃣ CONTACT DETAILS
# =========================================================
@app.post("/institution/{institution_id}/contacts")
def save_contacts(institution_id: str, data: Dict):
    """
    Stores:
    - principal
    - academic coordinator / placement head
    """
    data["institution_id"] = institution_id
    institution_contact_col.insert_one(data)
    return {
        "status": "success",
        "message": "Contact details saved"
    }

# =========================================================
# 3️⃣ ADDRESS DETAILS
# =========================================================
@app.post("/institution/{institution_id}/address")
def save_address(institution_id: str, data: Dict):
    """
    Stores:
    - country
    - state
    - district
    - city
    - area
    - pincode
    """
    data["institution_id"] = institution_id
    institution_address_col.insert_one(data)
    return {
        "status": "success",
        "message": "Address saved"
    }

# =========================================================
# 4️⃣ ACADEMIC DETAILS
# =========================================================
@app.post("/institution/{institution_id}/academics")
def save_academics(institution_id: str, data: Dict):
    """
    Stores:
    - degrees
    - departments
    """
    data["institution_id"] = institution_id
    institution_academic_col.insert_one(data)
    return {
        "status": "success",
        "message": "Academic data saved"
    }

# =========================================================
# 5️⃣ DIGITAL & SOCIAL PRESENCE
# =========================================================
@app.post("/institution/{institution_id}/digital")
def save_digital_presence(institution_id: str, data: Dict):
    """
    Stores:
    - website
    - linkedin
    - instagram
    - facebook
    """
    data["institution_id"] = institution_id
    institution_digital_col.insert_one(data)
    return {
        "status": "success",
        "message": "Digital presence saved"
    }

# =========================================================
# 🧪 TESTING HELPERS (OPTIONAL)
# =========================================================
@app.delete("/testing/clear-all")
def clear_all_testing_data():
    institution_basic_col.delete_many({})
    institution_contact_col.delete_many({})
    institution_address_col.delete_many({})
    institution_academic_col.delete_many({})
    institution_digital_col.delete_many({})
    return {
        "status": "cleared",
        "message": "All testing collections cleared"
    }
