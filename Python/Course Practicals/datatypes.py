#var_1 = 12383498482398238181841318489
#print(var_1)

# if we try adding 1 to it
#print(var_1 + 1)

# You can add different datatypes together
#var = 234
#var2 = 10.5
#print(var + var2)
# To check the type
#print(type(var + var2))
# You could always add the result of the addition in a third variable and print out the result
#var3 = var + var2 
#print(var3)
#print(type(var))
#print(type(var2))
#print(type(var3))

# If we choose to add a prefix to the numbers (Octal, Hexadecimal, Binary, Decimal), it converts it to their respective decimal values
var = 0o123
var2 = 0x123
var3 = 0b100
var4 = 100
print(var)
print(var2)
print(var3)
print(var4)

# For strings
name = "Divine Providence"
name2 = "CS faculty"
a = 1
b = 2
print(name)
print(type(name))
# You can fetch specific characters with subscript
print(name[0]) # All characters start counting from 0

# You can't concatenate strings to integers, only string to string
#print(name + a)
#print("name" + a)

#You can concatenate integer to integer, and string to string. If the numbers are in a single or double quote, it'll concatenate, because they are now recognized as strings, not integers.

print("123" + "1") # This won't add, just concatenate them without spacing
print(a + b) # This will add, because they are both integers

# If you want to ignore special characters
print("Jenny's Lectures") # This will print just fine, but suppose i want to do this
#print("Jenny's "Lectures"") we could skip this by using one backward slash for the places we want to skip
print("Jenny\'s \"Lectures\"") # This would work fine, as Jenny's, and "Lectures"
print("Jenny\'s \n \"Lectures\"") # This woiuld also work, but we could always skip it and print it out on one line.
print("Jenny\'s \\n \"Lectures\"") # This would print as Jenny's \n "Lectures"

# To multiply the result, we can do this
print(5 * "Jenny\'s \\n \"Lectures\"") # Since we are printing all on the same line, this would print 5 times on the same line

# Boolean
age = True # Boolean has to be capitalized, else, you'll produce a name error.
print(age)
print(type(age))