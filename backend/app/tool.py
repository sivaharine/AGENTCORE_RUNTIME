from .database import products_collection

def check_product(query):
    query_lower = query.lower()

    product = products_collection.find_one(
        {"name": {"$regex": query_lower, "$options": "i"}} #i for case sensitive search
    )

    if product:
        return product["name"], {
            "price": product["price"],
            "stock": product["stock"]
        }

    return None, None

