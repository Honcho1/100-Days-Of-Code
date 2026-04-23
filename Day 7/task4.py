# Keeping track of the player's lives
import random

word_list = ["aardvark", "baboon", "camel", "apple"]
chosen_word = random.choice(word_list)

lives = 6

stages = [
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

display = []

for letter in chosen_word:
    display.append("_")

game_over = False

while not game_over:
    print(stages[lives])
    print("".join(display))

    guess = input("Guess a letter: ").lower()

    correct_guess = False

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = guess
            correct_guess = True

    if not correct_guess:
        lives -= 1

        if lives == 0:
            game_over = True
            print(stages[lives])
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("".join(display))
        print("You win!")