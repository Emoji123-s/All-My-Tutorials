"""
A loop is a repetitive action. In Python, a for loop is more like an iterator, to traverse a sequence one by one, to do specific action on each item in that sequence

Syntax
                    for var_name in sequence:
                        statement(s)

Supposedly we have a list
                    names = ["Divine", "Dracula", "Damien", "Deepika"]
using a for loop to traverse through the list
                    for name in names:
                        print(names)
Here, the variable name "name" is set for each item in the variable sequence "names", and with the for loop, we can traverse through the list and print the names in that list. Here, all the names will be printed accordingly.
"""


names = ["Divine", "Dracula", "Damien"]
for i in names:
    print(i)
    if i == "Dracula":
        print("Hey, it's me")

numbers = [1, 2, 3, 4, 5]
squares = [] # As an empty list
for number in numbers:
    square = number ** 2
    squares.append(square)
print(squares)