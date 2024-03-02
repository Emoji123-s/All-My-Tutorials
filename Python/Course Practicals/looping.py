"""
Use a for loop to cycle through the numbers 1 - 21
Use modulus to check that the result is NOT EQUAL to 0
Print out the odd numbers


for i in range(1, 21):
    if ((i % 2) != 0):
        print("i = ", i)

# Rounding up figures
var1 = float(input("Enter a float: "))

print("Rounded to 2 decimal places: {:.2f}".format(var1))
"""

# Compound Interest
"""
Have the user enter their investment amount and their expected interest
Each year, their investment will increase by their investment + their investment * interest
Print out the earnings after a 10 years period


# User's Input
investment = int(input("Enter your investment amount: "))
interest = float(input("Enter your expected interest: ")) * .01 # This should round the figure to a percentage of 2 digits

# Increment in the investment 
for i in range(10):
    investment = investment + (investment * interest)

print("Money after 10 years: {:.2f}".format(investment))


# While loop - As long as a condition remains true, we can continue looping with a while loop. We do this when we don't know how many times we want to loop

import random # This will generate random numbers for us, and we can use the different functions associated with the import

rand_num = random.randrange(1, 51) # This should generate numbers from 1-50
# The value we are going to be incrementing has to be defined before the loop
i = 1
while (i != rand_num):
    i += 1

print("The random value is: ", rand_num)
"""

# The continue function is going to stop executing the code that remains in the loop, while break jumps completely out of the loop 
# Printing a pine tree
# use 1 while loop and 3 for loops, and should work with any number provided


