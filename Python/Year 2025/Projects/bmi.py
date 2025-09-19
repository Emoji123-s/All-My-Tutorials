# A program to calculate Body Mass Index (BMI)
# BMI = weight (kg) / height (m)^2, basically weight/(height * height)
# Example: weight = 70kg, height = 1.75m, BMI = 70/(1.75*1.75) = 22.86

# Taking input from the user, and storing it in a variable for easier access
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculating BMI
bmi = weight / (height * height)

# Outputting the BMI to the user
print("Your BMI is:", bmi)

"""
Alternatively, you can use the exponentiation operator to calculate height squared
bmi = weight / (height ** 2)
print("Your BMI is: " + str(bmi))

""" 
# Note: The BMI value can be used to determine if a person is underweight, normal weight, overweight, or obese based on standard BMI categories.    
# BMI Categories:
# Underweight = BMI < 18.5
# Normal weight = 18.5 <= BMI < 24.9
# Overweight = 25 <= BMI < 29.9
# Obesity = BMI >= 30

