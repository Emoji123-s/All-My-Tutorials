# Calculate BMI (Body Mass Index) i.e, weight / height**2. Take a weight in kg from the user(int), and height in metres as a float value.

weight = int(input("Enter your weight (In kg, numbers only): "))
height = float(input("Enter your height (In metres, numbers only): "))

# To calculate the BMI, the formula is
bmi = int(weight / (height**2)) # Because we want to print it as a whole number instead of float

# Since exponentation has a higher precedence,
print("Your BMI (Body Mass Index) is {} ".format(bmi))
# Or
# print("Your BMI (Body Mass Index) is " + str(bmi)) For Concatenation