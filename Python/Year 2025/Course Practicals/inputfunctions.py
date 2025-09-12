# Input Functions
# The input function is used to take input from the user in Python.
# It reads a line from input, converts it into a string (stripping a trailing newline), and returns that.
# Syntax: input(prompt)
# Example 1: Taking a simple input
name = input("Enter your name: ") #saving the input in a variable
print(name)

# By default, the input function takes input as a string, and returns it as a string.
# Example 2: Taking an integer input
age = int(input("Enter your age: ")) # converting the input string to an integer
print(age)

print("Hello" + " " + name )
print("Hello", input("Enter your name: ")) # taking input directly in the print function