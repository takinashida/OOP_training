import json

from classes import Product, Category
from config import ROOT_DIR

if __name__ == "__main__":
    with open(ROOT_DIR.joinpath("data", "products.json"), "r", encoding="utf-8") as f:
        products = json.load(f)

    for category in products:
        Category.name = category["name"]
        Category.description = category["description"]
        Category.products = category["products"]
        for product in category["products"]:
            Product.name = product["name"]
            Product.description = product["description"]
            Product.price = product["price"]
            Product.quantity = product["quantity"]


