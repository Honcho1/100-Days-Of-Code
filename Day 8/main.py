# Caesar Cipher Program
from art import logo

print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, cipher_direction):
    result_text = ""
    
    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            result_text += alphabet[new_position]

        else:
            result_text += letter

    print(f"The {cipher_direction}d text is {result_text}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(
        original_text=text,
        shift_amount=shift,
        cipher_direction=direction
    )

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye!")

