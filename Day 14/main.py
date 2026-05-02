# Higher Lower Game
import random
from art import logo, vs
from game_data import data

def get_random_account(used_account=None):
    """Pick a random account, ensuring it's not the same as the used_account."""
    choice = random.choice(data)
    while choice == used_account:
        choice = random.choice(data)
    return choice

def format_account(account, label):
    """Print a formatted description of an account."""
    print(f"Compare {label}: {account['name']}, a {account['description']}, from {account['country']}.")

    