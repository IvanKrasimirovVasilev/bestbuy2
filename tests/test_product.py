from unittest import result

import pytest
from products import Product, NonStockedProduct

def test_create_product():
    product = Product("Ivan test product", 1450, 100)

    assert product.name == "Ivan test product"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() is True


def test_create_product_with_empty_name():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)


def test_create_product_with_negative_price():
    with pytest.raises(ValueError):
        Product("Ivan test product", -1450, 100)


def test_product_becomes_inactive():
    product = Product("Ivan test product", 1450, 10)
    product.quantity = 0

    assert product.is_active() is False

def test_buy_product():
    product = Product("Ivan test product", 1450, 100)
    result = product.buy(3)

    assert product.is_active() is True
    assert product.quantity == 97
    assert result == 1450*3

def test_buy_too_many_products():
    product = Product("Ivan test product", 1450, 10)

    with pytest.raises(ValueError):
        product.buy(14)

def test_set_negative_price():
    product = Product("MacBook Air M2", 1450, 100)

    with pytest.raises(ValueError):
        product.price = -100

def test_set_new_price():
    product = Product("MacBook Air M2", 1450, 100)

    product.price = 1600

    assert product.price == 1600

def test_non_stocked_product_quantity_stays_zero():
    product = NonStockedProduct("Windows License", 125)

    product.quantity = 500

    assert product.quantity == 0