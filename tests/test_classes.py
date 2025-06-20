import pytest

from src.classes import Category, Product


@pytest.fixture
def get_product():
    return Product(name="phone", description="good phone", price=150.0, quantity=1)


@pytest.fixture
def get_category():
    return Category(name="phones", description="low quantity", products=[1, 2, 3])


def test_product(get_product):
    assert get_product.name == "phone"
    assert get_product.description == "good phone"
    assert get_product.price == 150.0
    assert get_product.quantity == 1


def test_category(get_category):
    assert get_category.name == "phones"
    assert get_category.description == "low quantity"
    assert get_category.products == [1, 2, 3]
    assert get_category.product_count == 3
    assert get_category.category_count == 1
