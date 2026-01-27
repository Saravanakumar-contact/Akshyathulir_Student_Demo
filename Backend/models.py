from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Address(BaseModel):
    country: str
    state: str
    district: str
    city: str
    area: str
    pinCode: str

class Contact(BaseModel):
    name: str
    email: EmailStr
    phone: str

class Institution(BaseModel):
    # Institution details
    institutionName: str
    institutionType: str
    yearEstablished: int
    naacGrade: str
    autonomousStatus: Optional[str] = None
    universityName: Optional[str] = None
    officialEmail: EmailStr

    # Degrees & departments
    degrees: List[str]
    departments: List[str]

    # Personal info
    firstName: str
    lastName: str
    email: EmailStr
    phone: str
    gender: str
    designation: str

    # Key contacts
    principal: Contact
    academicCoordinator: Optional[Contact] = None
    placementHead: Optional[Contact] = None

    # Address
    address: Address

    # Digital presence
    websiteUrl: str
    linkedinUrl: str
    instagramUrl: Optional[str] = None
    facebookUrl: Optional[str] = None
