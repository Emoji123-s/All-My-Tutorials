"""
A Money Hider Program. Make a 3x3 matrix, and let the user select which position he/she wants to hide their money. The user input should be 2 numbers, the first representing row and the second representing column. The spot they choose would be marked by X once the program runs. 

[1 1 1]
[1 1 1]
[1 1 1]

If a user inputs 32, the first number should be the row, and the second will be column i.e

[1 1 1]
[1 1 1]
[1 X 1]

If the user inputs 23

[1 1 1]
[1 1 X]
[1 1 1]

Remember that list indexing starts from zero
"""

# Prompt
print("Money Hider Program. Choose a spot to hide your money")
print("Original Matrix")

# Making the Matrix
row1 = [1, 1, 1]
row2 = [1, 1, 1]
row3 = [1, 1, 1]

print(f"{row1}\n{row2}\n{row3}") # Prints as a 3x3 matrix

# Making the nested list to hold the 3 rows
matrix = (row1,row2,row3) # print(matrix) To verify if it's working

# User Input
spot = input("Enter a 2-digit number to pick a spot : ")
        
# Indexing the values
rows = int(spot[0])
columns = int(spot[1])

# Supposedly the user inputs 32 as the spot, the first number will be the row from the nested list. Since the indexing stops at 2, even though we have a 3x3 matrix, we can subtract 1 from the row to match the matrix's indexing
row_select = matrix[rows - 1]

# Once in the row, the next is the column to mark. Therefore, we can represent this with any integer value, and we can -1 from the row_select to give the exact place to hide money. If we use X, we'll have to change the list to a string format.
row_select[columns - 1] = 0

# Printing
print(f"{row1}\n{row2}\n{row3}")