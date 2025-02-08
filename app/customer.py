import math
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = tuple(location)
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def distance_to(self, shop_location: list) -> float:
        return round(math.dist(self.location, shop_location), 2)

    def calculate_trip_cost(self,
                            shop: "Shop",
                            fuel_price: int) -> float:
        distance = self.distance_to(shop.location)
        fuel_cost = self.car.calculate_fuel_cost(distance * 2, fuel_price)
        product_cost = shop.calculate_product_cost(self.product_cart)
        return round(fuel_cost + product_cost, 2)

    def make_purchase(self, shop: "Shop", fuel_price: int) -> None:
        trip_cost = self.calculate_trip_cost(shop, fuel_price)

        print(f"\n{self.name} has {self.money} dollars")
        print(f"{self.name}'s trip to {shop.name} costs {trip_cost}")

        if trip_cost > self.money:
            print(f"{self.name} "
                  f"doesn't have enough money to make a purchase in any shop")
            return

        print(f"{self.name} rides to {shop.name}")

        self.location = shop.location

        shop.sell_products(self)

        # Return home
        print(f"\n{self.name} rides home")
        self.location = self.location
        self.money -= trip_cost
        print(f"{self.name} now has {round(self.money, 2)} dollars")
