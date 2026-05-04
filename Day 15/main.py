# Coffee Machine

from platform import machine


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
    
def make_coffee(drink_name):
    """Deduct ingredients and serve the drink."""
    ingredients = MENU[drink_name]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

def print_report():
    """Print current resource levels and profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        print_report()

    elif choice in MENU:
        if is_resource_sufficient(choice):
            payment = process_coins()
            if is_transaction_successful(payment, choice):
                make_coffee(choice)

    else:
        print("Invalid option. Please choose espresso, latte, or cappuccino.")