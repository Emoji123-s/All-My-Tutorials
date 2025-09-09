print(len("Divine Providence"))
print(len("12345"))
#print(len(12345)) This produces a type error, because an object of type 'int' has no len()

# I could always choose to add it to a variable
length = len("Divine Providence")
#print("Your name has " + length + " characters") This would produce a type error. We can convert it to a string with the following
print("Your name has " + str(length) + " characters")
print(type(str(length))) #OR store it in another varible
new_length = str(length)
print(type(new_length))

# Suppose we are doing another conversion

print(10+10) # This should give us 20
print("10" + "10") # This should give us 1010
print("10" + "10") # This is a string, and i want to convert it to an integer, i can add the int function beside each string to convert it, which would give me 20, i.e
print(int("10") + int("10")) #This should print out 20 just fine
# Or probably to a float
print(float("10") + int("10")) # This should print out 20.0 just fine

# What if we wanted to add the integer value of a name to an integer
name1 = "Divine"
name2 = "123"
#print(10 + int(name1))  This gives us an error, but let's try something else
print(10 + int(name2)) 

# 4th project to understand type casting. Take 2 inputs from the user, then add those 2 numbers.
var1 = input("Enter your first number: ")
var2 = input("Enter your second number: ")

print(float(var1) + int(var2))