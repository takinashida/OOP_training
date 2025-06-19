import json

from src.classes import Category, Product


def json_load(path_to_data: str) -> list:
    """
    Открывает json файлы
    :param path_to_data: путь до файла
    :return: список словарей
    """
    with open(path_to_data, "r", encoding="utf-8") as f:
        return json.load(f)


def get_classes(
    categ_list: list, Product: classmethod = Product, Category: classmethod = Category
) -> tuple:
    """
    Распределяет данные из списка словарей по классам
    :param categ_list: Список словарей
    :param Product: Класс Product
    :param Category: Класс Category
    :return: Кортеж из списков объектов класса
    """
    categories = []
    products = []
    for categ in categ_list:
        for prod in categ["products"]:
            temp = Product(
                name=prod["name"],
                description=prod["description"],
                price=prod["price"],
                quantity=prod["quantity"],
            )
            products.append(temp)
        temp = Category(
            name=categ["name"], description=categ["description"], products=products
        )
        categories.append(temp)
    return categories, products
