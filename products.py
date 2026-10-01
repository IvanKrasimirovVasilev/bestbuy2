from promotions import Promotion

class Product:
    """Represent a product in the store."""

    def __init__(self, name, price, quantity):
        """Create a product."""

        # Check data types
        if not isinstance(name, str):
            raise TypeError("Product name must be a string.")

        if not isinstance(price, (int, float)):
            raise TypeError("Product price must be a number.")

        if not isinstance(quantity, int):
            raise TypeError("Product quantity must be an integer.")

        # Check data values
        if not name:
            raise ValueError("Product name cannot be empty.")

        if price < 0:
            raise ValueError("Product price cannot be negative.")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    @property
    def price(self):
        """Return the product price."""
        return self._price

    @price.setter
    def price(self, value):
        """Set the product price."""
        if not isinstance(value, (int, float)):
            raise TypeError("Product price must be a number.")

        if value < 0:
            raise ValueError("Product price cannot be negative.")

        self._price = value

    @property
    def quantity(self):
        """Return the product quantity."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """Set the product quantity."""
        if not isinstance(value, int):
            raise TypeError("Product quantity must be an integer.")
        if value < 0:
            raise ValueError("Product quantity cannot be negative.")
        self._quantity = value

        if value == 0:
            self.deactivate()


    def get_quantity(self):
        """Return the product quantity."""
        return self.quantity

    def get_promotion(self):
        """Return the product promotion."""

        return self.promotion

    def set_promotion(self, promotion):
        """Set the promotion."""

        if promotion is not None and not isinstance(promotion, Promotion):
            raise TypeError("Promotion must be a Promotion object or None.")

        self.promotion = promotion

    def is_active(self):
        """Return whether the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def set_quantity(self, quantity):
        """Set the product quantity."""

        if not isinstance(quantity, (int)):
            raise TypeError("Wrong product quantity. Must be an integer.")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")


        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def show(self):
        """Display the product information."""
        output = (
                self.name + ", Price: " + str(self.price) +
                ", Quantity: " + str(self.quantity)
        )

        if self.promotion:
            output += ", Promotion: " + self.promotion.name

        print(output)

    def buy(self, quantity):
        """Buy a quantity of the product."""

        if not isinstance(quantity, (int)):
            raise TypeError("Wrong product quantity. Must be an integer.")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        # Check if product is active
        if not self.is_active():
            raise ValueError("Product is not active.")

        if quantity > self.quantity:
            raise ValueError("Not enough " + self.name +
                             "in store. We have only " + str(self.quantity) +
                             " items. Please make new order" )

        self.quantity -= quantity

        # Apply promotion if the product has one
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return quantity * self.price

class NonStockedProduct(Product):
    """Represent a non-stock product in the store."""
    def __init__(self, name, price):
        """Create a non-stock product."""
        super().__init__(name, price, 0)

    @property
    def quantity(self):
        """Return the product quantity."""
        return 0

    @quantity.setter
    def quantity(self, value):
        """Keep the product quantity always at zero."""
        self._quantity = 0

    def show(self):
        """Display non-stocked product information."""

        output = (
                self.name + ", Price: " + str(self.price) +
                ", Quantity: unlimited"
        )

        if self.promotion:
            output += ", Promotion: " + self.promotion.name

        print(output)

    def buy(self, quantity):
        """Buy a nonstocked product."""

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return quantity * self.price


class LimitedProduct(Product):
    """Represent a limited product in the store."""
    def __init__(self, name, price, quantity, maximum):
        """Create a limited product."""
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """Buy a limited quantity of the product."""

        if quantity > self.maximum:
            raise ValueError("Cannot buy more than the maximum quantity.")

        return super().buy(quantity)

    def show(self):
        """Display limited product information."""

        output = (
                self.name + ", Price: " + str(self.price) +
                ", Quantity: " + str(self.quantity) +
                ", Max order quantity: " + str(self.maximum)
        )

        if self.promotion:
            output += ", Promotion: " + self.promotion.name

        print(output)