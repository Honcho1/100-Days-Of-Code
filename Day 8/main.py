# Caesar Cipher Program
from unittest import result


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, cipher_direction):
    result_text = ""

    for letter in original_text:
        position = alphabet.index(letter)

        if cipher_direction == "encode":
            new_position = position + shift_amount
        elif cipher_direction == "decode":
            new_position = position - shift_amount

        result_text += alphabet[new_position % 26]

    print(f"The {cipher_direction}d text is {result_text}")

caesar(original_text=text, shift_amount=shift, cipher_direction=direction)