from art import logo
from replit import clear

print(logo)

bidding_finished = False
list_of_bidders = {}

# Given a dictionary of names and bids, find the person with the highest bid
def find_highest_bidder(bidding_list):
    highest_bidder = ''
    highest_bid = 0
    for bidder in bidding_list:
        bid_amount = bidding_list[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")


while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    list_of_bidders[name] = bid

    any_more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if any_more_bidders == 'no':
        bidding_finished = True
        find_highest_bidder(list_of_bidders)
    else:
        clear()
