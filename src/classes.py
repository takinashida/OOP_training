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

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __len__(self):
        return len(self.__products)

    def add_product(self, new_product):
        try:
            if isinstance(new_product, Product):
                self.__products.append(new_product)
        except TypeError as e:
            print(f"Это не продукт: {e}")
            return

    @property
    def products(self):
        return self.__products

    @property
    def str_products(self):
        result = []
        for product in self.products:
            result.append(str(product))
        return result


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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(self, Product) and isinstance(other, Product):
            return self.total_value() + other.total_value()

    def total_value(self):
        if isinstance(self, Product):
            return self.price * self.quantity

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
            quantity=product_dict["quantity"],
        )


class Iteration:

    def __init__(self, stop):
        if not isinstance(stop, Category):
            raise ValueError
        self.stop = stop

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index + 1 < len(self.stop.products):
            self.index += 1
            return self.stop.products[self.index]
        else:
            raise StopIteration
