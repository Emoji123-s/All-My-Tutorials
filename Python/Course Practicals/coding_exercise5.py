"""
Write a program to find out how many days, weeks and months we have left if we live until 90 years old
Input : Current Age
Output: A message containing "You have a days, b weeks and c months left"
1 year = 365 days
1 year = 52 weeks
1 year = 12 months(excluding the leap year)
"""
# Request input from the user
age_left = int(input("Enter your current age : "))

# If we are living up to 90 years
years = 90 - age_left

# Formula to calculate

# If 1 year = 365 days
days = 365 * years

# If 1 year = 52 weeks
weeks = 52 * years

# If 1 year = 12 months
months = 12 * years

# Print the result
print(f"You have {days} days, {weeks} weeks, and {months} months left")