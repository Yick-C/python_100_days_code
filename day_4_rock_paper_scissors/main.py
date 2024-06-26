import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
computer_choice = random.randint(0, 2)
choice = [rock, paper, scissors]
player_choice = 3

while player_choice > 2:
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    if (player_choice > 2):
        print("Please pick a valid number.")
    else:
        print(choice[player_choice])

print(f"Computer chose: \n{choice[computer_choice]}")

if ((player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (
        player_choice == 2 and computer_choice == 1)):
    print("You win!")
elif (player_choice == computer_choice):
    print("It's a draw")
else:
    print("You lose!")
