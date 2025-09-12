# A program to swap 2 given numbers
# Taking input from the user
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print("Before swapping: num1 =", num1, "num2 =", num2)
# Taking a temporary variable to hold one value during the swap
temp = num1 # move the first number to temp variable, making num1 empty
num1 = num2 # move the second number to first variable, filling num1 and making num2 empty
num2 = temp # move the temp variable to second variable, filling num2 and making temp empty
# Printing the swapped values
print("After swapping: num1 =", num1, "num2 =", num2)