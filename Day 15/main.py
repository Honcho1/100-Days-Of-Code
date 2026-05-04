# Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

resources = {
    "water": 300,    # ml
    "milk": 200,     # ml
    "coffee": 100,   # g
}

profit = 0

def is_resource_sufficient(drink_name):
    """Check if the machine has enough of each ingredient to make the drink."""
    ingredients = MENU[drink_name]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True