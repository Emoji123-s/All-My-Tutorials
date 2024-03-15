"""
Updated Version of BMI. Check if the person is underweight, overweight, or normal weight

Underweight - Severe thinness = < 16.0
Underweight - Moderate thinness = 16.0 - 16.9
Underweight - Mild thinness = 17.0 - 18.4
Normal Range - 18.5 - 24.9
Overweight - Pre-Obese = 25.0 - 29.9
Obese - Class 1 = 30.0 - 34.9
Obese - Class 2 = 35.0 - 39.9
Obese - Class 3 = >= 40.0
"""
# Input from the user

weight = int(input("Enter your weight (In kg, numbers only): "))
height = float(input("Enter your height (In metres, numbers only): "))

# To calculate the BMI, the formula is
bmi = (weight / (height**2)) # Because we want to print it as a whole number instead of float

# User Conditions
if (bmi < 16.0):
    print("Your Body Mass Index is : {:.1f}".format(bmi))
    print("You're Severely Thin")
elif (bmi <= 16.9):
    print("Your Body Mass Index is : {:.1f}".format(bmi))
    print("You're Moderately Thin")
elif (bmi <= 18.4):
    print("Your Body Mass Index is : {:.1f}".format(bmi))
    print("You're Mildly Thin")
elif (bmi <= 24.9):
    print("Your Body Mass Index is : {:.1f}".format(bmi))
    print("You're Normal Weight")
elif (bmi <= 29.9):
    print("Your Body Mass Index is : {:.1f}".format(bmi))
    print("You're Pre-Obese")
elif (bmi <= 34.9):
    print("Your Body Mass Index is : {:.1f}".format(bmi))
    print("You're Class 1 Obese")
elif (bmi <= 39.9):
    print("Your Body Mass Index is : {:.1f}".format(bmi))
    print("You're Class 2 Obese")
else:
    print("Your Body Mass Index is : {:.1f}".format(bmi))
    print("You're Class 3 Obese")