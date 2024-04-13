"""
A while loop is used to execute statement blocks until a given condition is true

Syntax
                    while condition/expression:
                        statement(s)

While loops are used when we don't know the number of times the statement will be executed

While-Else
Basically the reverse of for-else, the else block executes when the while loop becomes false. The else block will not execute if the while loop was terminated forcefully.

Syntax
                        while condition/expression:
                            statement(s)
                        else:
                            statement(s)
"""
# Incrementing
count = 1
while count <= 5:
    print(count)
    count += 1
print("Out of while loop")

# Decrementing
count1 = 5
while count1 > 0:
    print(count1)
    count1 -= 1
print("Out of while loop")

# Difference between for and while loop
number = int(input("Enter a number (-1 to quit) : "))
while number != -1:
    print(number)
    number = int(input("Enter a number (-1 to quit) : "))
else:
    print("In else block")
print("Out of while loop")

# Using Boolean values
count2 = 0
while True:
    print(count2)
    count2 += 1
    if count2 == 5:
        break
else:
    print("In else block")
print("Out of while loop")
