# Variables

# Program to print the length of user input string
name = input("Enter your name: ") # taking input from the user
print("Hello", name) # printing the input
print("Length of your name is:", len(name)) # printing the length of the input string


# Rules when naming a variable
# 1. It should be meaningful
# 2. It should not start with a number
# 3. It should not contain spaces
# 4. It should not be a reserved keyword in Python
# 5. It should not contain special characters except underscore (_)
# 6. It is case-sensitive
# Examples of valid variable names
my_name = "Alice"
age1 = 25
is_student = True
# Examples of invalid variable names (uncommenting these will cause errors)
# 1name = "Bob" # starts with a number
# my name = "Charlie" # contains space
# class = "Math" # reserved keyword
# my-name = "David" # contains special character '-'
# Demonstrating case sensitivity
var = 10
Var = 20
print("var =", var) # prints 10
print("Var =", Var) # prints 20