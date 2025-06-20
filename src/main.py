from config import ROOT_DIR
from src.utils import get_classes, json_load

if __name__ == "__main__":
    path_to_json = ROOT_DIR.joinpath("data", "products.json")

    categories, products = get_classes(json_load(path_to_json))

    print(categories, "\n", products)
    phones = categories[0]
    for phone in phones.products:
        print(phone.name)
