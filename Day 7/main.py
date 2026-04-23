# Hangman game
import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)

lives = 6

display = []
guessed_letters = []

for letter in chosen_word:
    display.append("_")

game_over = False

while not game_over:
    print(stages[lives])
    print(" ".join(display))

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed {guess}. Try a different letter.")
        continue

    guessed_letters.append(guess)

    correct_guess = False

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = guess
            correct_guess = True

    if not correct_guess:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(stages[lives])
            print("************************** YOU LOSE! **************************")

    if "_" not in display:
        game_over = True
        print(stages[lives])
        print("************************** YOU WIN! **************************")