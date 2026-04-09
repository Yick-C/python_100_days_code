#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    name_list = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_draft = letter_file.read()
    for name in name_list:
        stripped_name = name.strip()
        contents = letter_draft.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", 'w') as new_letter:
            new_letter.write(contents)
