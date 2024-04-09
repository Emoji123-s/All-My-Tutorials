"""
A Password Generator. Take input from the user, for amount of letters, amount of symbols, amount of numbers. From the user input, generate a password. There are 2 levels, the easy where the password isn't shuffled from the user input, and the hard level where the password is shuffled from the user input.

Easy
Generate random numbers and symbols. The password should take the amount of numbers, symbols and letters and form a password without shuffling. Exactly in the same order that was provided.

Hard
Generate random numbers and symbols. The password should take the amount of numbers, symbols and letters and form a password. This time, the password should be shuffled every time the program runs
"""

# For Easy

# Prompt Message
print("Password Generator")

# Importing Library
import random

# User Input
amount_of_letters = int(input("How many letters do you want in your password? "))
amount_of_symbols = int(input("How many symbols do you want in your password? "))
amount_of_numbers = int(input("How many numbers do you want in your password? "))

# Character Pool holding the uppercase, lowercase, symbols and numbers
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?`~"
numbers = '0123456789'

letters = uppercase_letters + lowercase_letters

# Using the random.choice module

password = ""
for i in range(amount_of_letters):
    password += random.choice(letters)

for i in range(amount_of_symbols):
    password += random.choice(special_characters)

for i in range(amount_of_numbers):
    password += random.choice(numbers)

# Printing the Password
print(password)