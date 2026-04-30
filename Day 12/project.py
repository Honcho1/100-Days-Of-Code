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
    
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = set_difficulty()

    game_over = False

    while not game_over:
        print(f"You have {attempts} attempts remaining.")

        guess = int(input("Make a guess: "))

        if check_guess(guess, number):
            game_over = True
        else:
            attempts -= 1

            if attempts == 0:
                print("You've run out of guesses,. You lose.")
                print(f"The number was {number}.")
                game_over = True
            else:
                print("Guess again.\n")

game()