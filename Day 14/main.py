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

def check_answer(user_answer, account_a, account_b):
    """Return True if the user's answer is correct, False otherwise."""
    if account_a['follower_count'] > account_b['follower_count']:
        correct_answer = 'a'
    else:
        correct_answer = 'b'
    return user_answer == correct_answer

def play_game():
    print(logo)
    score = 0
    account_a = get_random_account()
    game_over = False