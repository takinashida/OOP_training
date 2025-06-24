class Category:
    """Класс категорий товаров(Смартфоны, Трава и тд.)"""

    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int

    def __init__(self, name: str, description: str, products: list) -> None:
        """
        Метод инициации класса
        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов в данной категории
        """
        self.name = name
        self.description = description
        self.__products = list(products)
        self.product_count = len(products)
        self.category_count += 1

    def __str__(self) -> str:
        """
        dunder-метод __str__
        :return: Оформленная строка
        """
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __len__(self) -> int:
        """
        dunder-метод __len__
        :return: Количество продуктов в категории
        """
        return len(self.__products)

    def add_product(self, new_product) -> None:
        """
        Метод при помощи которого добавляют новые продукты
        :param new_product: Объект класса продукт
        :return: Ничего
        """
        if isinstance(new_product, Product):
            self.__products.append(new_product)
        else:
            raise TypeError("Это не продукт")
        return

    @property
    def products(self) -> list:
        """
        Возвращает список
        :return: список продуктов
        """
        return self.__products

    @property
    def str_products(self) -> list:
        """
        Метод возвращает список товаров в качестве оформленых строк
        :return: список продуктов
        """
        result = []
        for product in self.products:
            result.append(str(product))
        return result


class Product:
    """Класс продукта(тип смартфона или вид травы)"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Метод инициации класса
        :param name: Название категории
        :param description: Описание категории
        :param price: Цена продукта за шт
        :param quantity: Количество продукта на складе
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """
        Дандр метод __str__
        :return: Возвращает строку
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """
        Дандр метод __add__
        :param other: объект с которым нужно складывать
        :return: сумма 2 продуктов одной категории
        """
        if type(self) == type(other):
            return self.total_value() + other.total_value()
        else:
            raise TypeError("Вы пытаетесь сложить 2 разных товара")

    def total_value(self) -> float | None:
        """
        Общая стоимость товаров
        :return: Произведение цены и количества
        """
        if isinstance(self, Product):
            return self.price * self.quantity

    @property
    def price(self) -> float:
        """
        Возвращает цену
        :return: Цена
        """
        return self.__price

    @price.setter
    def price(self, new_price: int) -> None:
        """
        Заменяет цену на новую
        :param new_price: Новая цена
        :return: Ничего
        """
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
        """
        Добавляет новый продукт
        :param product_dict: Словарь с новым продуктом
        :param products: Список с объектами Product
        :return: Объект класса Product
        """
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
    """Класс для итерации"""

    def __init__(self, stop):
        """
        Метод инициации класса
        :param stop: Объект класса Category
        """
        if not isinstance(stop, Category):
            raise ValueError("Это не категория")
        self.stop = stop

    def __iter__(self) -> iter:
        """
        Дандер метод __iter__
        :return: Итерируемый объект
        """
        self.index = -1
        return self

    def __next__(self):
        """
        Дандер метод __next__
        :return: Объект Product
        """
        if self.index + 1 < len(self.stop.products):
            self.index += 1
            return self.stop.products[self.index]
        else:
            raise StopIteration


class Smartphone(Product):
    """Дочерний класс от Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """
        Метод инициации класса
        :param name: Имя смартфона
        :param description: Описание смартфона
        :param price: Цена смартфона
        :param quantity: Количество смартфона
        :param efficiency: Эффективность смартфона
        :param model: Модель смартфона
        :param memory: Количество памяти смартфона
        :param color: Цвет смартфона
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Дочерний класс от Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """
        Метод инициации класса
        :param name: Имя газона
        :param description: Описание газона
        :param price: Цена газона
        :param quantity: Количество газона
        :param country: Страна-производитель
        :param germination_period: Время проращивания
        :param color: Цвет газона
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
