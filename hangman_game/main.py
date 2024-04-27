# Step 1
import random
from hangman_words import word_list
from hangman_art import logo, stages

end_of_game = False
word_list = word_list

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)
lives = 6

print(logo)
# Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = list("_" * chosen_word_length)
print(''.join(display))

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}!")
    # Check guessed letter
    for position in range(chosen_word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If guess is not a letter in the chosen_word,
    #     #Then reduce 'lives' by 1.
    #     #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.")
        if lives == 0:
            end_of_game = True
            print("You lost!")

    print(' '.join(display))

    if "_" not in display:
        end_of_game = True
        print("You won!")

    print(stages[lives])
