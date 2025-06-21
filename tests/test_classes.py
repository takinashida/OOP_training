from unittest.mock import patch

import pytest

from src.classes import Category, Product


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


def test_product(get_product):
    assert get_product.name == "phone"
    assert get_product.description == "good phone"
    assert get_product.price == 150.0

    assert get_product.quantity == 1


# @patch(src.classes.self.__products)
def test_category(get_category):
    assert get_category.name == "phones"
    assert get_category.description == "low quantity"
    assert get_category.products[0].name == "phone"
    assert get_category.str_products == ["phone, 150.0 руб., Остаток: 1 шт."]
    assert get_category.product_count == 1
    assert get_category.category_count == 1
