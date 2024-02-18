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