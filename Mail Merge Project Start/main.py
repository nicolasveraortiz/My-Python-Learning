# TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as letter:
    letter = letter.read()
# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names:
    names = names.read().splitlines()
# Replace the [name] placeholder with the actual name.
for name in names:
    new_letter = letter.replace("[name]", f"{name}")
    with open(f"./Output/ReadyToSend/{name}Invitation.txt", mode="w") as readyletter:
        readyletter.write(new_letter)

# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
