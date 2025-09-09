"""
Write a program to find out how many days, weeks and months a user has left according to the user's age and the number of years they choose to live
Input : Current Age
Output: A message containing "You have a days, b weeks and c months left"
1 year = 365 days
1 year = 52 weeks
1 year = 12 months(excluding the leap year)
"""

# User Input
age = int(input("Enter your current age (Numbers only) : "))
years = int(input("How long do you want to live (Input in years only) : "))

# To get the approximate number they choose to live
total = years - age

# Conditons if the user decides to be crazy :)
if(age > years):
    print("Invalid Format, Years > Age")
else:
    # Formula

    # If 1 year = 365 days
    days = 365 * total

    # If 1 year = 52 weeks
    weeks = 52 * total

    # If 1 year = 12 months
    months = 12 * total

    # printing
    print(f"You have {days} days, {weeks} weeks, and {months} months left")

if (age == 0):
    print("0 is not a valid age")
    
if(age == years):
    print("You aren't a living being anymore :'(")