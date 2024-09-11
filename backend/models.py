from pymongo import MongoClient

MONGO_URL = "mongodb+srv://vansh8010:12345@doctor.bwmcb.mongodb.net/?retryWrites=true&w=majority&appName=doctor"
client = MongoClient(MONGO_URL)
db = client["db1"]
collection = db["patient"]
