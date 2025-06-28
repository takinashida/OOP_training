from unittest.mock import patch

import pytest

from src.classes import (BaseOrder, BaseProduct, Category, Iteration,
                         LawnGrass, NullException, Order, Product, Smartphone)


@pytest.fixture
def get_product():
    return Product(name="phone", description="good phone", price=150.0, quantity=1)


@pytest.fixture
def get_category():
    return Category(
        name="phones",
        description="low quantity",
        products=[Product(name="phone", description="good phone", price=150.0, quantity=1)],
    )


@patch("builtins.input")
def test_price_setter(mock_input):
    fake_input = " Y"
    phone = Product(name="phone", description="good phone", price=150.0, quantity=1)
    mock_input.return_value = fake_input
    phone.price = 100
    assert phone.price == 100
    fake_input = " неа"
    mock_input.return_value = fake_input
    phone.price = 80
    assert phone.price == 100
    phone.price = -500
    assert phone.price == 100


def test_new_products():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        category1.products,
    )
    assert category1.products[0].quantity == 10

    category1.add_product(
        Product.new_product(
            {
                "name": "Sosung Galaxy S24 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
            category1.products,
        )
    )
    assert len(category1.products) == 4
    assert product1 + product2 == 3480000.0
    assert str(list(Iteration(category1))[0]) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 10 шт."


def test_product(get_product):
    assert get_product.name == "phone"
    assert get_product.description == "good phone"
    assert get_product.price == 150.0
    assert get_product.quantity == 1


def test_category(get_category):
    assert get_category.name == "phones"
    assert get_category.description == "low quantity"
    assert get_category.products[0].name == "phone"
    assert get_category.str_products == ["phone, 150.0 руб. Остаток: 1 шт."]
    assert get_category.product_count == 1
    assert get_category.category_count == 2
    assert str(get_category) == "phones, количество продуктов: 1 шт."
    assert len(get_category) == 1


@pytest.fixture()
def get_smartphones():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


def test_smartphone(get_smartphones):
    smartphone = get_smartphones
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


@pytest.fixture()
def get_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


def test_grass(get_grass):
    grass = get_grass
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_add_product():
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", ["smartphone1", "smartphone2"])
    with pytest.raises(TypeError) as e:
        category_smartphones.add_product("Not a product")
    assert str(e.value) == "Это не продукт"


def test_add_in_product():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError) as e:
        smartphone + grass
    assert str(e.value) == "Вы пытаетесь сложить 2 разных товара"


def test_raise_iteration():
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    with pytest.raises(ValueError) as e:
        Iteration(grass)
    assert str(e.value) == "Это не категория"


def test_order():
    product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    order = Order(product, 1)
    assert order.link == product
    order.add_product(Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 2))
    assert str(order) == '55" QLED 4K, количество продуктов: 3 шт.'
    with pytest.raises(TypeError) as e:
        order.add_product("Not a product")
    assert str(e.value) == "Это не продукт"


def test_abstract():
    with pytest.raises(TypeError):
        BaseProduct()

    with pytest.raises(TypeError):
        BaseOrder()


def test_NullException(capsys):
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    captured = capsys.readouterr()
    assert (
        captured.out
        == """Нельзя добавить ноль товаров
Обработка добавления товара завершена
"""
    )


def test_null_product():
    with pytest.raises(ValueError):
        product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)


def test_avg_price():
    category = Category(
        name="phones",
        description="low quantity",
        products=[
            Product(name="phone", description="good phone", price=150.0, quantity=1),
            Product(name="phone", description="good phone", price=450.0, quantity=1),
        ],
    )
    assert category.avg_price() == 300.0
    category = Category(name="phones", description="low quantity", products=[])
    assert category.avg_price() == 0
