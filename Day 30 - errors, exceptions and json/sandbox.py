# File not found
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["bjrfehbg"])
except FileNotFoundError:
    open("a_file.txt", 'w')
    print("There was an error")
except KeyError as error_message:
    print(f"Key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height cannot be over 3 meters.")

bmi = weight / height ** 2
print(bmi)