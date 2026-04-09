from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

isOff = False

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while not isOff:
    order = input(f"What would you like? ({menu.get_items()}): ")

    if order == 'off':
        isOff = True
        print("Thank you for using this service. Have a lovely day! Turning off now.")

    elif order == 'report':
        coffee_machine.report()
        money_machine.report()

    elif not menu.find_drink(order):
        print("Please try again")

    else:
        drink = menu.find_drink(order)
        if not coffee_machine.is_resource_sufficient(drink):
            print("Please try again later.")
        else:
            priceOfDrink = drink.cost
            if money_machine.make_payment(priceOfDrink):
                coffee_machine.make_coffee(drink)

