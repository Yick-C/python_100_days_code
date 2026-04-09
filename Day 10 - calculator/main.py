from art import logo

# Calculator
def add(n1, n2):
    """ Adds two numbers together """
    return n1 + n2

def subtract(n1, n2):
    """ Subtract two numbers together """
    return n1 - n2

def multiply(n1, n2):
    """ Multiply two numbers together """
    return n1 * n2

def divide(n1, n2):
    """ Divide two numbers together """
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


print(logo)

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    isFinished = False

    while not isFinished:
        operation_symbol = input("Pick another operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continueCalc = input(f"Type 'y' to continue calculating with {answer}, or type"
                             f"'n' to start a new calculation.: ")

        if(continueCalc == 'y'):
            num1 = answer
        else:
            isFinished = True
            calculator()

calculator()