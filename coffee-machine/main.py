from machine_data import MENU

# Coins
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

profit = 0
isOff = False

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def calculateMoney(quarters, dimes, nickles, pennies):
    total = (quarters * QUARTERS) + (dimes * DIMES) + (nickles * NICKLES) + (pennies * PENNIES)
    return total

def checkResources(order):
    isEnoughResource = True
    ingredients = MENU[order]["ingredients"]
    for resource in ingredients:
        if MENU[order]["ingredients"][resource] > resources[resource]:
            isEnoughResource = False
            return isEnoughResource

    return isEnoughResource

def makeCoffee(order):
    ingredients = MENU[order]["ingredients"]
    for resource in ingredients:
        resources[resource] = resources[resource] - MENU[order]["ingredients"][resource]

while not isOff:
    # Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    order = input("What would you like? (espresso/latte/cappuccino): ")

    # Turn off the Coffee Machine by entering “off” to the prompt
    if order == 'off':
        isOff = True
        print("Thank you for using this service. Have a lovely day! Turning off now.")

    # Print report
    elif order == 'report':
        print(f"\n===Current resources=== \nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")

    elif order == 'latte' or order == 'espresso' or order == 'cappuccino':
        # Check resources sufficient?
        if not checkResources(order):
            print("Sorry the coffee machine does not have enough resources for this order.")
        else:
            print(f"Okay you have ordered one {order}.\n")

            # Process coins.
            print("Please insert coins. ")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            moneyPaid = calculateMoney(quarters, dimes, nickles, pennies)

            if moneyPaid > MENU[order]["cost"]:
                profit += moneyPaid
                change = round(moneyPaid - MENU[order]["cost"], 2)
                print(f"Here is ${change} in change.\n")

                makeCoffee()
                print(f"Here is your {order} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")

    else:
        print("That was not a valid order, please try again.")
