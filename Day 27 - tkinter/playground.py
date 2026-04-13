# Positional Arguments: position matters!
# *args will let you add as many arguments as you want
# *args is a tuple so if you print it e.g. (1, 4, 5, 6)
def add(*args):
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1, 4, 5, 6))

# Keyword Arguments
# **kwargs
def calculate(n, **kwargs):
    print(kwargs)  # is a dictionary
    for key, value in kwargs.items():
        print(key)
        print(value)

    print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")  # Using .get() is better as it returns 'none' instead of an error
        self.model = kw.get("model")  # Instead of using kw["model"]
        self.colour = kw.get("colour")

my_car = Car(make="Nissan")
print(my_car.model)


# Output of this code
# 4 (7, 3, 0) { 'x': 10, 'y': 64 }
def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)