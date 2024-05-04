# A game of Higher or Lower where two random Instagram accounts are given, and you
# must guess which account has more followers (A or B). The game will end when the
# wrong answer is given

from art import logo, vs
from game_data import data
import random

def compareFollowers(celeb_A, celeb_B):
    """Given two objects from game_data, returns the one who has the
    higher follower count, either 'A' or 'B'."""
    compareA_followers = celeb_A["follower_count"]
    compareB_followers = celeb_B["follower_count"]

    if(compareA_followers > compareB_followers):
        return 'A'
    else:
        return 'B'


## Start game of Higher or Lower
print(logo)
hasLost = False
score = 0

while not hasLost:
    compareA = random.choice(data)
    compareB = random.choice(data)
    while compareA == compareB:
        compareB = random.choice(data)

    print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}.")
    print(f"Against B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B: ")

    if(guess == compareFollowers(compareA, compareB)):
        score += 1
        print(f"You're right! Current score: {score}. \n")
    else:
        hasLost = True
        print(f"Sorry, that's wrong. Final score: {score}")