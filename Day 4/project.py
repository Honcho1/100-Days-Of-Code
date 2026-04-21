#Rock Paper Scissors Game

import random

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
if user_choice == "0":
    print("You chose Rock.")
elif user_choice == "1":
    print("You chose Paper.")
elif user_choice == "2":
    print("You chose Scissors.")
else:
    print("Invalid choice. Please choose 0, 1, or 2.")

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print("Computer chose Rock.")
elif computer_choice == 1:
    print("Computer chose Paper.")
elif computer_choice == 2:
    print("Computer chose Scissors.")

if user_choice == "0" and computer_choice == 2:
    print("You win!")
elif user_choice == "1" and computer_choice == 0:
    print("You win!")
elif user_choice == "2" and computer_choice == 1:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")
else:
    print("You lose!")

