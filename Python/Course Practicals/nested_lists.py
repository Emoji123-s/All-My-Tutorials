"""
A nested list is a list within a list i.e
"""
numbers = [1, 10, 15, [20, 25, 30], 17, 0]

# If we find out the length of the list
print(len(numbers)) # It counts the entire list inside that list as one.

# Let's check the index of the nested list
print(numbers[3]) # This will print the numbers stored at index 3

# We can go further
print(numbers[3][1]) # This will go into the nested list, and print out the number stored at index 1


lists = [10, 34, 90, [45, 78, -3], 89]
print(lists[len(lists) -2])

# Slicing
print(lists[3][0:3]) # we provided the start point and end point, so it'll print the complete list
print(lists[3][0:]) # This should print the same thing, because we provided the start, and automatically, the length of the list is the end
print(lists[3][0:2]) # This prints the numbers at the length of 2, whic is 45 and 78

# Steps
print(lists[3][::2]) # this would print the starting number at 0, then skip 78 because it is at 1, and print -3, because it is at step 2
