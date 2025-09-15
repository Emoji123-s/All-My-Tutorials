# Type Casting / Type Conversion

# Length of a string
print(len("Divine Providence")) # you can also count numbers too, but it has to be in quotes
#print(len(12345)) Uncommenting this will produce a type error, because it is an integer value

# using a variable
length = len("Divine")
print(length)

# Let's try concatenating
print("Hi, your name has", length, "characters") # Using comma automatically converts it to a string, which is so much easier than a + symbol

# with a + symbol
#print("Hi, your name has" + length + "characters") Uncommmenting this will give a type error

# Using type conversion with the + symbol
print("Hi, your name has " + str(length) + " characters")

# checking the type
# Let's save the converted length in a new variable
new = str(length)
print(type(length))
print(type(new))



""" (* multi-line comment)
Others include
int()
float()
str()
"""

# program to take input from the user, specifically 2 numbers and add that input

num1 = int(input("Enter your first number: ")) # as a string, then converted to integer
num2 = int(input("Enter your second number: ")) # as a string

# Adding the numbers together
print(num1 + num2)