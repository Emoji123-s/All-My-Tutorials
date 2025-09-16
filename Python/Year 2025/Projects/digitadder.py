# Program to add digits of a number
"""
If the user puts in 12 as a digit, the output should be 3, basically adding the individual digits of the numbers
"""

# Taking input from the user, and storig it in a variable for easier access
user_input = input("Enter a 2 digit number: ")

# Storing the individual value of each digit in separate variables
num1 = int(user_input[0])

num2 = int(user_input[1])

# Adding the individual variables together
sum = num1 + num2
print(sum)
