from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://127.0.0.1:27017/")
DB_NAME = os.getenv("DB_NAME", "days_to_week_convertor")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "conversions")