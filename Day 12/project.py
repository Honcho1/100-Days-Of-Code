# Number Guessing Game

import random


def check_guess(user_guess, actual_number):
    if user_guess > actual_number:
        print("Too high.")
        return False
    elif user_guess < actual_number:
        print("Too low.")
        return False
    else:
        print(f"You got it! The number was {actual_number}.")
        return True
    
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return 10
    else:
        return 5