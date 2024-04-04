"""
Sets are also used to store multiple items in a single variable name, but in curly brackets. In sets, duplicates are not allowed, because once you print the set, then only one type of the duplicated element will be printed. Also, they do not have any defined order i.e, unordered. When they are printed, it is not guaranteed that the order of sequence will be the same as the order specified in the set.

Syntax
                        set1 = {10, True, "Divine", 1.11}
                        set2 = {1, 2, 10, -3} = Integer
                        set3 = {"Divine", "Damien", "Dracula"}

If
                        set4 = {1, 10, 20, 4, 5, 9}
Once printed, it might be
                                {10, 1, 9, 5, 4, 20}

                                
Properties

1.  Indexing is not allowed on sets, because they are unordered every time they are printed
2.  Duplicate items are not allowed, because only one occurrence of the item will be printed
3.  They are unordered, so a definite position of an item in a list is not guaranteed to be that same position once it it printed.
4.  Set items are unchangeable i.e you cannot change the items
                                set2[2] = 30 - It is not possible
5.  A set can be completely changed, i.e items can be added and removed 
6.  A set can be homogeneous. It can have different datatypes
7.  Since True = 1 and 1 is an integer, if both are placed in a set, only one will be printed i.e
                            set1 = {10, True, "Divine", 1.11, 1}
8.  Slicing is not allowed either
9.  Sets can take tuples, because tuples are immutable, unlike tuples that are immutable
"""

set1 = {10, 56, 89, 90, "Divine", True}
set4 = {10, 56, 89, 90, "Divine", True}
print(set1)
print(type(set1))

# Empty Set
set2 = {}
print(set2)
print(type(set2)) # The type is defined as a dictionary instead of a set

# To create an empty set
set3 = set()
print(set3)
print(type(set3))

# Add a value
set1.add(99)
print(set1)

# Length of the set
print(len(set1))

# Remove an item
set1.remove(10)
print(set1)

# Discard
set1.discard(89)
print(set1) # If the element is not present, the discard method will do nothing and return the set the way it was

# Clear the set
set1.clear()
print(set1)

# Pop
set4.pop() # Removes any random item from the set. It could be anything
print(set4) # If all the items are popped, it'll raise an exception

# While adding, we can add any immutable item that cannot be changed
set4.add((2, 3, 4)) # Adding a tuple is allowed
print(set4)
print(len(set4))