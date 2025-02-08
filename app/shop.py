from datetime import datetime
from typing import Any


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = tuple(location)
        self.products = products

    def calculate_product_cost(self, product_cart: dict) -> float:
        total_cost = 0
        for item, quantity in product_cart.items():
            if item in self.products:
                total_cost += self.products[item] * quantity
        return round(total_cost, 2)

    def sell_products(self, customer: Any) -> None:
        total_cost = self.calculate_product_cost(customer.product_cart)
        print("\nDate:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for item, quantity in customer.product_cart.items():
            if item in self.products:
                item_cost = self.products[item] * quantity
                print(f"{quantity} {item}(s) for {item_cost} dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
