"""
Program to calculate the average height from a list of heights. You cannot use sum and len functions. You have to replicate their functionalities with the help of for loop. You have to take input from the user using input function. The output should be rounded to a whole number. You can use the split function to split the user input, then the range function
"""
# Message Prompt
print("Average Height Program")

# User input
heights = input("Enter the minimum and maximum height separated by a comma : ")

# Splitting
list1 = heights.split(",")
mini = int(list1[0])
maxi = int(list1[1])

# since we can't use len and sum, we can replicate it
count = 0 # This is for the len replication, to count the number of items in the list
total_height = 0 # This is for the sum replication, to hold the sum of each instance of the heights

# Using For loop to traverse through the list
for i in range(mini, maxi + 1): # This adds 1 to the max value, and prints out the intended maxi value
    total_height = total_height + i # since i will be assigned to each item in the list, we can add the items in i and store them in the variable total_height
    count = count + 1 # For every height, count will increase by 1
    print(i)
average_height = total_height / count

print(f"The average height is {round(average_height)}")