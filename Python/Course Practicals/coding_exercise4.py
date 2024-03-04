# Print odd numbers from 1-20. Use a for loop and range, and use if and modulus to print out the odds.

for i in range(21):
    if((i % 2) != 0):
        print("Odd number is ", i)



# Compound Interest. Have the user enter their investment amount and their expected interest earned each year. Formula is investment + investment * interest. Print it out after a 10 year period

investment = int(input("Enter your investment amount: "))
interest = float(input("Enter your interest rate: ")) * .01 

# After 10 years. Since we are going for 10 years
for i in range(10):
    investment = investment + (investment * interest)

print("After 10 Years: {:.2f}".format(investment))
