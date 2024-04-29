from art import logo
from random import randint

EASY_MODE = 10
HARD_MODE = 5

print(logo)
print("Welcome to the Number Guessing game!\n")
print("I'm thinking of a number between 1 and 100")

guess = 0
target_number = randint(1, 100)
# print(f"psst, the correct answer is {target_number}")

def play_game():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attempts = EASY_MODE
    else:
        attempts = HARD_MODE

    while attempts != 0:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("\nMake a guess: "))

        if guess == target_number:
            print("Correct guess!")
            return
        elif guess < target_number:
            print("Too low.")
        else:
            print("Too high.")

        attempts -= 1

    print("\nYou've run out of guesses, you lose.")

play_game()