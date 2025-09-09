"""
In cases where we want to check one more condition after a particular condition has been checked, we can use multiple if. The general syntax is
if condition 1:
    do x
if condition 2:
    do y
if condition 3:
    do z

What if we wanted to add a photo price to the rolercoaster ride
"""

name = input("Enter your Name : ")
print(f"Hi {name}, fill out the following")

height = int(input("Enter your height in feet : "))

if (height >= 3):
    print("You can ride")
    age = int(input("How old are you ? "))

    if (age <= 12):
        print("You are to pay 1500 naira")
        photos = input("Do you want to take photos? (Yes or No) ")
        if (photos == "Yes"):
            print("A photo is 100 naira per photo.")
            number = int(input("How many photos will you be taking? "))
            number = number * 100
            print(f"Total amount is {number + 1500}")
        else:
            print("Pay 1500 naira")

    elif (age <= 18):
        print("You are to pay 2500 naira")
        photos = input("Do you want to take photos? (Yes or No) ")
        if (photos == "Yes"):
            print("A photo is 100 naira per photo.")
            number = int(input("How many photos will you be taking? "))
            number = number * 100
            print(f"Total amount is {number + 2500}")
        else:
            print("Pay 2500 naira")

    elif (age > 18):
        print("You are to pay 5000 naira")
        photos = input("Do you want to take photos? (Yes or No) ")
        if (photos == "Yes"):
            print("A photo is 100 naira per photo.")
            number = int(input("How many photos will you be taking? "))
            number = number * 100
            print(f"Total amount is {number + 5000}")
        else:
            print("Pay 5000 naira")
else:
    print("Too short for this ride")