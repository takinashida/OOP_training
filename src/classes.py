from abc import ABC, abstractmethod
from pyexpat.errors import messages


class Mixin:
    """Класс доп функциональности"""

    def __init__(self, *args, **kwargs):
        name_class = self.__class__.__name__
        print(f"{name_class} {args}")
        super().__init__()


class BaseOrder(ABC):
    """Базовый класс от которого зависит класс Category и Order"""

    __slots__ = ()

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def add_product(self, new_product) -> None:
        pass


class NullException(Exception):
    """Класс для вызова ошибки при попытке добавления продукта с нулевым количеством."""

    def __init__(self, message="Нельзя добавить ноль товаров"):
        self.message = message

    def __str__(self):
        return self.message


class Order(BaseOrder, Mixin):
    """Класс заказов зависящий от абстрактного класса BaseOrder"""

    __slots__ = ("link", "quantity")

    def __init__(self, link, quantity):
        super().__init__()
        self.link = link
        try:
            if quantity == 0:
                raise NullException()
            else:
                self.quantity = quantity
        finally:
            print("Обработка добавления товара завершена")

    def __str__(self) -> str:
        """
        dunder-метод __str__
        :return: Оформленная строка
        """
        return f"{self.link.name}, количество продуктов: {self.quantity} шт."

    def add_product(self, new_product) -> None:
        """
        Метод при помощи которого добавляют количество нового продукта
        :param new_product: Объект класса продукт
        :return: Ничего
        """
        if isinstance(new_product, Product) and self.link.name == new_product.name:
            self.quantity += new_product.quantity
        else:
            raise TypeError("Это не продукт")
        return


class Category(BaseOrder, Mixin):
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
        try:
            if len(products) == 0:
                raise NullException()
            else:
                self.product_count = len(products)
        except NullException:
            print("Нельзя добавить ноль товаров")
        finally:
            print("Обработка добавления товара завершена")
        Category.category_count += 1

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

    def avg_price(self) -> float | int:
        """
        Рассчитывает среднюю стоимость 1 товара в категории
        :return: средняя стоимость товара, если товаров нет 0
        """
        avg = 0
        for prod in self.products:
            avg += prod.price
        try:
            avg /= len(self.products)
        except ZeroDivisionError:
            return 0
        else:
            return round(avg, 2)

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


class BaseProduct(ABC):
    """Базовый класс от которого зависит класс Product"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def total_value(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_dict: dict, products: list):
        pass


class Product(Mixin, BaseProduct):
    """Класс продукта(тип смартфона или вид травы)"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)
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
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
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
