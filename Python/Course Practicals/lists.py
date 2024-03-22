"""
A list is a collection of elements enclosed in square brackets, seperated by a comma. It is a dynamically sized array that doesn't need to be homogeneous. It is mutable, i.e, it can change or can be altered. It is a data structure that helps in storing and organizing data. It falls under Sequenced Datatypes, because it contains sequence of data. Examples are
roll_number = [1, 2, 3, 4, 5] - List of Integers
names = ["Divine", "Ariana", "Isaac"] - List of Strings
mix_list = [1, "Divine", True, 10.10] - Mixed list containing integer, string, boolean and float

To print

print(roll_number)

To print individual elements of a list, supposedly i want to print the number 3 in the roll_number list

print(roll_number[2]) - Because counting starts from zero(0) in programming

Lists can also contain duplicates, i.e,
roll_number = [1, 2, 3, 4, 5, 2, 1] - List of Integers
"""

numbers = [10, 0, -1, 7]
print(numbers)

names = ["Divine", "Ariana", "Isaac"]
print(names)

mix_list = [1, "Divine", True, 10.10, -64, 8, 11]
print(mix_list)
print(mix_list[1]) # To access individual characters
print(len(mix_list)) # To check the length of the list
print(mix_list[-1]) # Negative index is allowed, and it'll print 10.1
print(mix_list[0:4]) # Starting from index zero(0), and the length of the list. This should print out the entire list.
print(mix_list[:]) # By default, starting point will be zero, and the end will be the length of the list
print(mix_list[0:]) # By default, it'll take the length of the variable list, and will print the entire list
print(mix_list[1:3]) # 1 is the starting point, and 3 is the length of the index to be sliced, so it'll print "Divine" and "True", because "Divine" was on index 1, and "True" was on index 2. If it's 1:2, only "Divine" will be printed
print(mix_list[0:5:2]) # This is extended slicing, and the last digit represent a step to be skipped before printing. With this, starting from index zero(0), it jumps 2 steps and prints True, then jumps 2 more steps and prints -64.
print(mix_list[0:5:3])

# Special Functions
# Sort
numbers.sort()
print(numbers) # This sorts the list
print(numbers.sort()) # This will print nothing, because the sort function returns nothing

# Reverse
numbers.reverse()
print(numbers) # This reverses the list

# Min and Max
print(min(numbers)) # Prints the minimum from the list
print(max(numbers)) # Prints the maximum from the list

# Append
numbers.append((45)) # At the end of a list, one element at a time can be added
print(numbers)

# Insert
numbers.insert(2, 90) # This will take 2 values, the first as the index you want to insert, and the second is whatever you want to add. This doesn't replace the value at index 2, rather it just inserts the value 45 in the list at index 2.
print(numbers)

# Extend
numbers.extend([60, 47, 48, 78, 89]) # This takes a list, and the values are joined with the existing list. The list is joined with the end of the list. It is just like append, except you can add moe values/elements
print(numbers)

# Change
numbers[1] = 45 # This changes the value of whatever index is passed to it.
print(numbers)
# also
numbers[1:4] = [45, 46, 47] # This will change the values of the index stored at 1 to 3, because 4 is the length of the list
print(numbers)

# Remove
numbers.remove(45) # This removes the first occurence of the value passed to it. 
print(numbers)

# Pop
print(numbers.pop()) # Returns the element it removed by default
numbers.pop() # Removes the last element by default
print(numbers)
print(numbers.pop(1)) # Removes specific index passed to it
print(numbers)