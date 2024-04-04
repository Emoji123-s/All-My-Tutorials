"""
Nested If
It is basically an if statement inside an if statement

if condition1:
    statement1
    if condition2:
        statement2

Any number of nested if is possible. The indentation in python is key to identify the level of nesting

Nested If-Else
It is considered if a complete if-else construct is within an if or an else block.

if condition1:
    statement1
    if condition2:
        statement2
    else:
        statement3
else:
    statement4 - It can also be situated here


# Nested If-Else - Rollercoaster Ride
# If you are more than or equal to 3 feet, you can ride, and if your age is less than or equal to 18, you will pay 250 naira, and if it is  greater than 18, you'll pay 500 naira

# Age from the user, and probably the name for future documentation
name = input("Enter your Name : ")
print(f"Hi {name}, fill out the following")

height = int(input("Enter your height in feet : "))

if (height >= 3):
    print("You can ride")
    age = int(input("How old are you ? "))
    if (age <= 18):
        print("Pay 250 naira")
    else:
        print("Pay 500 naira")
else:
    print("Too short for this ride")
print("Bye!")
"""

"""
Elif

It means else-if, and it is used for multiple case statements
Supposedly we wanted to add if age > 12 for 150, then if age is between 12-18, then greater than 18 is 500


name = input("Enter your Name : ")
print(f"Hi {name}, fill out the following")

height = int(input("Enter your height in feet : "))

if (height >= 3):
    print("You can ride")
    age = int(input("How old are you ? "))
    if (age <= 12):
        print("Pay 1500 naira")
    elif (age <= 18):
        print("Pay 2500 naira")
    elif (age > 18):
        print("Pay 5000 naira")
else:
    print("Too short for this ride")
"""

"""
If a user enters 1, it should print One, if 2, it should print 2, if 3, should print 3
"""
print("Number Familiarization")
# Take number from the user
number = int(input("Enter a number : "))

# Conditions
if (number == 1):
    print(f"{number} - This is number One")
elif (number == 2):
    print(f"{number} - This is number Two")
elif (number == 3):
    print(f"{number} - This is number Three")
elif (number == 4):
    print(f"{number} - This is number Four")
else:
    print("Wrong Input")