import json


def load_config(filename: str) -> list:
    with open(filename, "r") as file:
        return json.load(file)
