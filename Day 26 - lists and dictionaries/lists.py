# Creating a new list from another list
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# === Using List Comprehension === #
# new_list = [new_item for item in numbers]
new_list_improved = [n + 1 for n in numbers]

# List Comprehension doesn't have to be just for lists
name = "Angela"
letters_list = [letter for letter in name]

# List Comprehension for range
range_list = [n * 2 for n in range(1, 5)]  # starting list is [1, 2, 3, 4]

# Conditional List Comprehension
# new_list_cond = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

caps_name = [name.upper() for name in names if len(name) > 5]

# Create a list called result which contains the numbers that are common in both files.
# The output should be a list of integers and not strings!
with open("file1.txt") as f1, open("file2.txt") as f2:
    file1_list = [int(num) for num in f1.readlines()]
    file2_list = [int(num) for num in f2.readlines()]

result = [num for num in file1_list if num in file2_list]