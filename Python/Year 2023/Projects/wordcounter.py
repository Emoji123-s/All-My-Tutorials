"""
Create a program that counts the number of words in a user-inputted sentence or paragraph.
Concatenate the user input into a single string.
Use the split() method to split the string into words and count the number of elements in the resulting list.
Print the word count using the print function.
"""

# First, we take input from the user
sentence = input("Enter your sentence / text: ")

# Do we need to concatenate anything? Since the user input is already a string format.
# We need to split the sentence into words and count them

word = sentence.split()

# Then print the resulting word count
print("Word Count:", len(word))