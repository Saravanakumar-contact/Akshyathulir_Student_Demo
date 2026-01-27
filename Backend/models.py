from pydantic import BaseModel, EmailStr

class Institution(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str

class User(BaseModel):
    name: str
    email: EmailStr
