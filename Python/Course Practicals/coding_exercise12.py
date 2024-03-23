"""
Who will pay the bill? Select a random name from a list of names and the person selected has to pay for everyone's food bill. Take names from the user, and once that is done, the program should print who will pay the bill from the list of names. Use the split function to split into a list

import random

# User Input
names = input("Enter names seperated by a comma : ")

# Spliting the names 
names_split = names.split(",") # This should turn it into a list
print(names_split)

# Accessing names
name_random = random.choice(names_split)

# Printing
print(f"{name_random} will pay the bill :D")

"""

# OR
import random

# User Input
names = input("Enter names seperated by a comma: ")

# Splitting the names
names_split = names.split(",")

# Since we don't know the length of the list, and how many names the user will input, we can find the length of the list
name_length = len(names_split)

# Let's assign an index value to the list
name_random = random.randint(0, name_length - 1) # If the list is supposedly 10 names, the length of the list will be 10, but the index will count from zero(0) and stop at 9. So the namelength will be -1 to match the index

# To print using subscript
print(f"{names_split[name_random]} will pay the bill") # From the split list, a random name will be chosen everytime using the indexed number