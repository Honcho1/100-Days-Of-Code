# Check if the player has won the game

import random

word_list = ["aardvark", "baboon", "camel", "apple"]
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Check each position
    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = guess

    print("".join(display))

    # If no blanks remain, the player has won
    if "_" not in display:
        game_over = True
        print("You win!")