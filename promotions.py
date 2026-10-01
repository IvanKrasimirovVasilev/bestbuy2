"""Promotion classes for product discounts."""
from abc import ABC, abstractmethod

class Promotion(ABC):
    """Represent a product promotion."""

    def __init__(self, name):

        if not isinstance(name, str):
            raise TypeError("Promotion name must be a string.")

        if not name:
            raise ValueError("Promotion name cannot be empty.")

        self.name = name

    @abstractmethod
    def apply_promotion(self, product,  quantity):
        pass

class PercentDiscount(Promotion):
    """Represent a percent discount promotion."""

    def __init__(self, name, percent):
        super().__init__(name)

        if not isinstance(percent, (int, float)):
            raise TypeError("Percent must be a number.")

        if percent < 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100.")

        self.percent = percent

    def apply_promotion(self, product, quantity):
        """Represent a percent discount promotion."""
        total_price = product.price * quantity
        discount = total_price * self.percent / 100
        result = total_price - discount

        return result

class SecondHalfPrice(Promotion):
    """Represent a second item half price promotion."""

    def apply_promotion(self, product, quantity):
        """Represent a second item half price promotion."""
        half_price_items = quantity // 2
        total_price = product.price * quantity
        discount = half_price_items * product.price / 2
        result = total_price - discount

        return result

class ThirdOneFree(Promotion):
    """Represent a third product free promotion."""

    def apply_promotion(self, product, quantity):
        """Represent a third product free promotion."""
        free_items = quantity // 3
        total_price = product.price * quantity
        discount = free_items * product.price
        result = total_price - discount

        return result
