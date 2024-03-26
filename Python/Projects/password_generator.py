"""
Develop a password generator that asks the user for the desired length of the password and the type of characters to include (e.g, letters, numbers, symbols)
Concatenate randomly selected characters to generate the password
Print the generated password using the print function
"""

import random
# Prompt Message
print("Paswword Generator")

# User Input
length = int(input("How long do you want the password to be? "))
character_type = input("Type of characters to be included (Numbers, Letters, Symbols), seperated by a comma: ")

# Splitting the String 
character_type_split = character_type.split(",")

# Random
character_random= random.choice(character_type_split)
character_sample = random.sample(character_type_split, length)
character_print = print(f"{character_sample}")