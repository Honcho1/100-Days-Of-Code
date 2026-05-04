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

def process_coins():
    """Ask user to insert coins and returns total value in dollars."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total

def is_transaction_successful(money_received, drink_name):
    """Check if the user paid enough; refund or return change if needed."""
    cost = MENU[drink_name]["cost"]
    if money_received >= cost:
        change = round(money_received - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False