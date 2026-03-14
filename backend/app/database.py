from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["customer_support"]
products_collection = db["products"]

def get_product_from_db(query):# mongodb query
    return products_collection.find_one(
        {"name": {"$regex": query, "$options": "i"}}
    )

#$regex-Used for pattern matching
#"$options": "i":  "i" → Case-insensitive search