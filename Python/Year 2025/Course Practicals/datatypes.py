# Datatypes in Python
# The functon type() is used to know the datatype of a variable

print(type("Hello")) # String

# Types of datatypes

# Integer
# Whole numbers, positive or negative, without decimals, has unlimited length
num1 = 100
print(0b1100100) # Binary representation of 100
print(0o144) # Octal representation of 100
print(0x64) # Hexadecimal representation of 100
print(100) # Decimal representation of 100
print(type(num1)) # prints <class 'int'>

# Float
# Decimal numbers, positive or negative, with decimals, limited precision
num2 = 10.5
print(num2)
print(type(num2)) # prints <class 'float'>

# String
# Sequence of characters, enclosed in single or double quotes
name = "Divine Providence"
print(name)
print(type(name)) # prints <class 'str'>

# Boolean
# Represents one of two values: True or False
bool1 = True
bool2 = False
print(bool1)
print(bool2)
print(type(bool1)) # prints <class 'bool'>
print(type(bool2)) # prints <class 'bool'>  