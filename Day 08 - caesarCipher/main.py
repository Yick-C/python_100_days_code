from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Caesar function that can encrypt and decrypt text
def caesar(start_text, shift_amount, cipher_direction):
    result_text = ''
    if (cipher_direction == 'decode'):
        shift_amount *= -1
    for char in start_text:
        # Keep the number/symbol/space when the text is encoded/decoded
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            result_text += alphabet[new_position]
        else:
            result_text += char

    print(f"The {direction}d text is {result_text}")


# Start program
should_continue = True
print(f"\033[36m{logo}\033[00m")

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # The program continues to work even if the user enters a shift number greater than 26
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to continue encoding/encoding. Otherwise, type 'no'\n")
    if(result == 'no'):
        should_continue = False
        print("Thanks for using this encoding/decoding program.")





# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

# def encrypt(text, shift):
#     encrypted_text = ''
#     for char in text:
#         index = alphabet.index(char) + shift
#         if(index >= len(alphabet)):
#             index -= len(alphabet)
#         encrypted_text += alphabet[index]
#     print(f"The encoded text is {encrypted_text}")
#
# def decrypt(text, shift):
#     print("Decrypt")
#     decrypted_text = ''
#     for char in text:
#         index = alphabet.index(char) - shift
#         if(index <= 0):
#             index -= len(alphabet)
#         decrypted_text += alphabet[index]
#     print(f"The decrypted text is {decrypted_text}")