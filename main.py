import products
import store
import promotions


# Create list of products
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

product_list[0].show()

best_buy = store.Store(product_list)


def make_order(store_obj):
    """Create and process a customer order."""
    shopping_list = []
    active_products = store_obj.get_all_products()

    for index, product in enumerate(active_products):
        print(str(index + 1) + ". ", end="")
        product.show()

    while True:
        try:
            product_number = int(
                input("Which product do you want? (0 to finish): ")
            )
        except ValueError:
            print("Invalid input. Please enter a product number.")
            continue

        if product_number == 0:
            break

        if product_number < 0 or product_number > len(active_products):
            print(
                "Invalid product number. "
                "Please choose a product from the list."
            )
            continue

        selected_product = active_products[product_number - 1]

        try:
            quantity = int(
                input(
                    "How many " + selected_product.name +
                    " would you like to order? "
                )
            )
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        shopping_list.append((selected_product, quantity))

    try:
        total_price = store_obj.order(shopping_list)
        print("Order cost: " + str(total_price))

    except (TypeError, ValueError) as error:
        print("Order failed: " + str(error))
        return [], 0

    return shopping_list, total_price


def start(store_obj):
    """Run the store menu."""
    order_history = []
    total_order_price = 0

    while True:
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            for product in store_obj.get_all_products():
                product.show()

        elif choice == "2":
            print(store_obj.get_total_quantity())

        elif choice == "3":
            shopping_list, total_price = make_order(store_obj)

            order_history.extend(shopping_list)
            total_order_price += total_price

        elif choice == "4":
            if order_history:
                print("\nYour order:")

                for product, quantity in order_history:

                    if product.get_promotion():
                        price = product.get_promotion().apply_promotion(product, quantity)
                    else:
                        price = quantity * product.price

                    print(
                        str(quantity) + " x " + product.name +
                        " - " + str(price) + " euro"
                    )
                print("\nTotal price: " + str(total_order_price) + " euro")

            print("Thank you and goodbye!")
            break

        else:
            print(
                "Invalid choice. "
                "Please choose a number between 1 and 4."
            )


if __name__ == "__main__":
    start(best_buy)
