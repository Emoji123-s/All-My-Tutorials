"""
Write a program to check whether a given year is a leap year or not

1. How to calculate a leap - A leap year is 366 days, with 29 days in February
2. A leap year happens every 4 years, so since were in 2024, the last leap year would be 2024 - 4 , to give 2020.
"""

# Display Message
print("Leap Year Checker")

# Input from the user
year = int(input("Enter a given year to check: "))

# Since a leap year happens every 4 years
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")