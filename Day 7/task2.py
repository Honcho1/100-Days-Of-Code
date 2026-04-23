# Replacing blanks with guessed letters

import random

word_list = ["aardvark", "baboon", "camel", "apple"]
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for letter in chosen_word:
    display.append("_")

print("".join(display))

guess = input("Guess a letter: ").lower()

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print("".join(display))
