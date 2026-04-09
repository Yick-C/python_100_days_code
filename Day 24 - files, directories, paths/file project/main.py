# An example of how to open the file but need to remember to close it
# Rather than keeping it open, closing it saves resources, like closing your tabs in browser
# file = open("my_file.txt")
# file.close()

# Reads, opens and closes file when done
# with open("my_file.txt") as file:
#     contents = file.read()

# Default is read-only mode 'r'. To overwrite the file, change it to 'w'. To add to it, use 'a'
# It can create a new file if it doesn't exist, and it's in 'w' mode
with open("my_file.txt", mode="a") as file:
    file.write("New text.")
