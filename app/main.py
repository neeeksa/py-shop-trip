from app.data_json import load_config
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config = load_config(r"config.json")
    fuel_price = config["FUEL_PRICE"]
    shops = [
        Shop(s["name"], s["location"], s["products"]) for s in config["shops"]
    ]

    customers = [
        Customer(
            c["name"], c["product_cart"], c["location"], c["money"], c["car"]
        )
        for c in config["customers"]]

    for customer in customers:
        cheapest_shop = None
        cheapest_cost = float("inf")

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            if trip_cost < cheapest_cost:
                cheapest_cost = trip_cost
                cheapest_shop = shop

        if cheapest_shop:
            customer.make_purchase(cheapest_shop, fuel_price)


if __name__ == "__main__":
    shop_trip()
