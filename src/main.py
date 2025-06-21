from config import ROOT_DIR
from src.classes import Category, Product
from src.utils import get_classes, json_load

if __name__ == "__main__":
    path_to_json = ROOT_DIR.joinpath("data", "products.json")

    categories, products = get_classes(json_load(path_to_json))

    phones = categories[0]
    new = []
    for prod in phones.products:
        new.append({"name": prod.name,"description": prod.description, "price": prod.price, "quantity": prod.quantity})
    print(new)
    # phone = {"name": "iphone","description": "None", "price": 150, "quantity": 1}
    # new_1 = Product.new_product(new, phone)
    # for phone in phones.products:
    #     print(phone)

