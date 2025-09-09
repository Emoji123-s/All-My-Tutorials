"""
It is basically trying to access an index that isn't there
"""
names = ["Divine", "Damien", "Dracula"]

# Generally, index starts from zero(0), to access any one, just pass in the index
print(names[1]) # This should print Damien, because it is stored at index 1
# But if we pass in 3
#print(names[3])  This will give an index error, because we have at index 2, even though there are 3 items in the list

# One simple way is to find out the length of the list
length = len(names) # This will give you 3.
print(length)

# Or
print(names[length-1]) # If we pass in just length, it will result in the same error, but a -1 prints out the last element in the list, rhyming with the index

# Or with Negative Index
print(names[-1]) # This would print "Dracula", because it is stored at index -1.
# if we do print(names[-4]), this would produce the same error because there is no index -4.