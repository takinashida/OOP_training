class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            agree = input("Цена снижается. Продолжить? (y/n): ")
            if agree.strip().lower() != "y":
                print("Действие было отменено")
                return
        self.__price = new_price


    @classmethod
    def new_product(cls, product_dict: dict, products: list):
        for product in products:
            if product_dict["name"] == product.name:
                product.quantity += product_dict["quantity"]
                product.price = max(product_dict["price"], product.price)
                return product
        return cls(
        name=product_dict["name"],
        description=product_dict["description"],
        price=product_dict["price"],
        quantity=product_dict["quantity"]
        )




class Category:
    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = list(products)
        self.product_count = len(products)
        self.category_count += 1


    def add_product(self, new_product):
        self.__products.append(new_product)


    @property
    def products(self):
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб., Остаток: {product.quantity} шт.")
        return result





