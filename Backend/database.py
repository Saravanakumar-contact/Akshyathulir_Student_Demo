from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["akshaya_thulir_test"]

institution_basic_col = db["institutions_basic"]
institution_contact_col = db["institutions_contacts"]
institution_address_col = db["institutions_address"]
institution_academic_col = db["institutions_academics"]
institution_digital_col = db["institutions_digital"]
