"""
Write a program to check whether given number is even or odd
"""

# User input
number = int(input("Enter a number to be evaluated : "))

# To check
if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")