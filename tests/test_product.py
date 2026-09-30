from unittest import result

import pytest
from products import Product

def test_create_product():
    product = Product("Ivan test product", 1450, 100)

    assert product.name == "Ivan test product"
    assert product.price == 1450
    assert product.get_quantity() == 100
    assert product.is_active() is True


def test_create_product_with_empty_name():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)


def test_create_product_with_negative_price():
    with pytest.raises(ValueError):
        Product("Ivan test product", -1450, 100)


def test_product_becomes_inactive():
    product = Product("Ivan test product", 1450, 10)
    product.set_quantity(0)

    assert product.is_active() is False

def test_buy_product():
    product = Product("Ivan test product", 1450, 100)
    result = product.buy(3)

    assert product.is_active() is True
    assert product.get_quantity() == 97
    assert result == 1450*3

def test_buy_too_many_products():
    product = Product("Ivan test product", 1450, 10)

    with pytest.raises(ValueError):
        product.buy(14)