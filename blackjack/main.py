############## Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Blackjack Game #####################

from art import logo
import random

def deal_card():
    """ Returns a random card from a deck of cards """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def startingDeck(arr):
    """ Deals two random cards to a player to set up for the game"""
    card1 = deal_card()
    card2 = deal_card()
    arr.append(card1)
    arr.append(card2)
    return arr

def calculateSum(cards):
    """ Calculate the sum of the cards and also check for blackjacks where
    the cards include an ace and a ten. """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compareScore(userScore, dealerScore):
    """ Given two scores, compare which one wins blackjack and return a print statement """
    if userScore > 21 and dealerScore > 21:
        return "You went over. You lose "

    if userScore == dealerScore:
        return "\nDraw! "
    elif dealerScore == 0:
        return "\nLose, opponent has Blackjack! "
    elif userScore == 0:
        return "\nWin with a Blackjack !"
    elif userScore > 21:
        return "\nYou went over 21. You lose "
    elif dealerScore > 21:
        return "\nThe dealer went over 21. You win! "
    elif userScore > dealerScore:
        return "\nYou win! "
    else:
        return "\nYou lose! "

def play_game():
    """ A function to play a round of Blackjack"""
    print(logo)
    usersCards = []
    dealersCards = []
    game_has_ended = False

    usersCards = startingDeck(usersCards)
    dealersCards = startingDeck(dealersCards)

    while not game_has_ended:
        userSum = calculateSum(usersCards)
        dealerSum = calculateSum(dealersCards)

        print(f"Your cards: {usersCards}, current score: {userSum}")
        print(f"Dealer's first card: {dealersCards[0]}")

        # Check if the user or dealer has blackjack, or if the user has a score
        # of over 21. If not, asks the user if they want to draw another card
        if userSum == 0 or dealerSum == 0 or userSum > 21:
            game_has_ended = True
        else:
            drawCard = input("Type 'y' to get another card, type 'n' to pass: ")
            if (drawCard == 'y'):
                usersCards.append(deal_card())
            else:
                game_has_ended = True

        ## Dealer will keep drawing cards as long as their score is less than 17
        while dealerSum != 0 and dealerSum < 17:
            dealersCards.append(deal_card())
            dealerSum = calculateSum(dealersCards)

        # Show the final results of the game
        print(f"\nYour final hand: {usersCards}, final score: {userSum}")
        print(f"Dealer's final card: {dealersCards}, final score: {dealerSum}")
        print(compareScore(userSum, dealerSum))
        game_has_ended = True


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()