import products
from products import Product


class Store:
    """Represent a store with products."""

    def __init__(self, products):
        """Create a store with a product list."""

        #check data type
        if not isinstance(products, list):
            raise TypeError("products must be a list.")

        #check that all products are objects
        for product in products:
            if not isinstance(product, Product):
                raise TypeError("Wrong product type. All products must be product object.")

        self.products = products

    def add_product(self, product):
        """Add a product to the store."""

        if not isinstance(product, products.Product):
            raise TypeError("Wrong product type. All products must be product object.")

        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""

        if not isinstance(product, products.Product):
            raise TypeError("Wrong product type. All products must be product object.")

        if product not in self.products:
            raise ValueError("Product not in store.")

        self.products.remove(product)

    def get_total_quantity(self):
        """Return the total quantity of all products."""
        total = 0
        for product in self.products:
            total += products.quantity

        return total

    def get_all_products(self):
        """Return all active products."""
        active_products = []

        for product in self.products:
            if product.is_active():
                active_products.append(product)

        return active_products

    def order(self, shopping_list):
        """Process an order and return the total price."""
        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
