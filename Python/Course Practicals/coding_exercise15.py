"""
Program to find out the maximum number from a list of numbers. Take the input from the user and split them. Do not use the inbuilt function max. replicate the functionality and use the range function.
"""

# Message Prompt


print("Max Value Finder")

# User Input
numbers = input("Enter a list of numbers separated by a space : ")

# Splitting
numbers_split = numbers.split(" ")

# Initializing variables
count = 0

# Replicating the len function
for number in numbers_split:
    count += 1
print(f"Count is {count}")

# Using for loop
for i in range(count):
    numbers_split[i] = int(numbers_split[i])  # type: ignore

# Replicating the max function
max_num = numbers_split[0] # Assuming the first number in the list is the max number, we can compare it with each element in the list.  
for i in numbers_split:
    if i > max_num:
        max_num = i
print(f"Max Value is {max_num}")