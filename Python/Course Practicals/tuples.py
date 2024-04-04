"""
A tuple is also used to store multiple items, but this time, in round brackets(parentheses). Tuples are immutable i.e unchangeable, unlike lists. Once you create a tuple, you can't add, remove or append anything to it

Syntax
                    tuple1 = (1, 10, -10, 15, 20) - Integer
                    tuple2 = ("Divine", "Dracula", "Damien") - String
                    tuple3 = (10, "divine", True, 10.5) - Mixed

If you create a tuple with one value i.e
                    tuple4 = (10) - Python won't recognize this as a tuple. There has to be a comma behind it to be recognized as a tuple
                    tuple5 = (10,)

We can check the type as well
                    print(type(tuple4))
                    print(type(tuple5))
"""

tuple1 = (12, 6, -8, 'Divine', True, 6, 12) # Duplication is allowed
tuple2 = (45, 67, 90)

print(tuple1)

# Indexing
print(tuple1[3])
print(tuple1[-2])

# Type Checking
print(type(tuple1))
print(type(tuple2))

# Immutable
#tuple1[0] = 13 - This won't work because tuples cant be changed once created

# Slicing
print(tuple1[1:]) # Prints to the last element in the tuple by default, but starts from index 1
print(tuple1[1:4]) # Prints to the third index 
print(tuple1[:4]) # Starts from the first index to index 3

# Steps
print(tuple1[::2]) # Skips one step and prints the number after it

# Length
print(len(tuple1))

# Nesting
tuple3 = (tuple1, tuple2)
print(tuple3)

print(tuple3[1]) # Prints the tuple at index 1
print(len(tuple3)) # Prints the number of each tuple

# Concatenation
tuple4 = tuple1 + tuple2
print(tuple4) # Merges the tuples together
print(len(tuple4)) # Counts the individual items in the tuple

# Min and Max
#print(min(tuple1))  Error, because the tuple is a mixture of string and integer
print(min(tuple2)) # tuple2 is an integer tuple
print(max(tuple2)) # Same as above

# Count
print(tuple1.count(12))

# Index Spotter
print(tuple1.index(12)) # Prints the index of the first occurrence of the element passed to it. If it is not there, it returns an error

# Convert List to Tuple
list1 = [1,2,3,4,5]
print(tuple(list1)) # Converts a list to a tuple

# Tuple Multiplication
tuple5 = (10,) * 5
print(tuple5)