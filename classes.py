class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        Product.name = name
        Product.description = description
        Product.price = price
        Product.quantity = quantity

class Category:
    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int


    def __init__(self, name, description, products):
        Category.name = name
        Category.description = description
        Category.products = list(products)
        Category.product_count = len(products)
        Category.category_count += 1

