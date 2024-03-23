"""
Coin Toss Program. Print for the user head or tails. 0 means tail and 1 means head. Simply generate a number between 0 and 1 and tell if that number is tail or head
"""

# Import the module
import random

# Generate number between 0 and 1 and store in a variable
number = random.randrange(0, 2)

# Condition
if (number == 0):
    print("Tails")
elif (number == 1):
    print("Heads")