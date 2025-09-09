# Write a program to add 2 digits number.
# If a user enters for instance, 12, the output should be 1+2, which would be 3.

print("Program to add a 2-digit number")
# let's take input from the user
var1 = input("Enter a 2-digit number only, e.g, 12, 05: \n")
# We want to add the digits together

sum = int(var1[0]) + int(var1[1]) # Using subscript, we can select each of the integer values stored in var1 and since input type is string, we need to convert them to integer and add them together.
print("Your number was " + str(var1))
print("Sum of your number is " + str(sum))