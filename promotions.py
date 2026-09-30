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
        total_price = product.price * quantity
        discount = total_price * self.percent / 100
        result = total_price - discount

        return result


class SecondHalfPrice(Promotion):
    """Represent a second item half price promotion."""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        half_price_items = quantity // 2
        total_price = product.price * quantity
        discount = half_price_items * product.price / 2
        result = total_price - discount

        return result

class ThirdOneFree(Promotion):
    """Represent a third product free promotion."""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        total_price = product.price * quantity
        discount = free_items * product.price
        result = total_price - discount

        return result