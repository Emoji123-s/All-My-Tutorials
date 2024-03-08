# It is regarded as f-strings because it is prefixed with the letter "f"
name = "Divine" # String
age = 30 # Integer
height = 1.6 # Float
# We want to print it in one line. First, we can concatenate
print("My name is", name,  ". I am", age, "years old", "and I'm", height, "m tall.")
# OR
print("My name is " + name +  " . I am " + str(age) + " years old and I'm " + str(height) + "m tall.")
# OR
print("My name is {}".format(name), ". I am {} years old".format(age), "and I'm {}m tall.".format(height))

# Using F-string
print(f"My name is {name}. I am {age} years old and I'm {height}m tall.")
# With f-strings, you dont need the commas. In the curly braces, write the variables to be evaluated, rather than concatenating them. The variables in the curly braces will be replaced by the words "Divine", "30" and "1.6", even though they are all of different datatypes. If we choose to make it an expression

print(f"Currently, I am {age*2} years old") # Ordinarily, this would print out (age*2) without the f prefix in place, but with it there, it'll be evaluated and print out 60

"""
Adavntages
1.  Easy
2.  Less Error-Prone
3.  More concise way to format strings
4.  Faster way to convert strings
5.  Evaluates directly at runtime
"""