"""
Love Calculator. Write a program to find a bonding between you and another user's name
User's Name and the love recipient
if your love score is < 10 or >= 70, they go together like coke and mentos
if your lovescore is >=40 and <=50, they are alright together
else, just print the lovescore
Using TRUE LOVE as a guide

A N K I T  R A O
N I S H A  J A I N

T R U E  L O V E 
1 1 0 0  0 1 0 0
   2       1        = 21%

   Print the score as a concatenated integer, not summed together

   
Python is case-sensitive, so a and A would be different characters. Use the lower function to turn it into lowercase ie
name.lower

and the count function to count i.e
name.count
"""

# User Input
name1 = input("Enter your First and Last Name : ")
name2 = input("Enter his/her First and Last Name : ")

# Let's combine them into one string
combined_name = name1 + name2 # We can cnocatenate string formats

# Incase the user inputs an uppercase, we need to make it lowercase
lowercase_name = combined_name.lower()

# To check using T R U E L O V E as a format, we need to count each letter of the word "TRUE LOVE", in the comnbined lowercase string, ans save them into desired variables
t = lowercase_name.count('t')
r = lowercase_name.count('r')
u = lowercase_name.count('u')
e = lowercase_name.count('e')

l = lowercase_name.count('l')
o = lowercase_name.count('o')
v = lowercase_name.count('v')
e = lowercase_name.count('e')

# Once counted, we can add up the letters into one variable
true = t + r + u + e # Since we're counting, it automatically goes into an integer format
love = l + o + v + e # Same as above

# We need to concatenate/combine, so that the result should be 21 instead of 2 + 1 = 3. So we'll save this into a variable

lovescore = int(str(true) + str(love)) # true and love variables are now in integer format, because of the count function. Since we want to print the result as a combined integer, rather than it adding together, we can convert true and love back to string format, then wrap them in an int to print it out as a concatenated value.

# Conditions
if lovescore < 10 or lovescore >= 70:
    print(f"Your lovescore is {lovescore} and you go together like coke and mentos :D ")
elif lovescore >= 40 and lovescore <= 50:
    print(f"Your lovescore is {lovescore} and you're alright together :) ")
else:
    print(f"Your lovescore is {lovescore}")