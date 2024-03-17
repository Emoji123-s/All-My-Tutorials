"""
Love Calculator. Write a program to find a bonding between you and another user's name
User's Name and the love recipient
if your love score is < 10 or > 90,
Using TRUE LOVE as a guide

A N K I T  R A O
N I S H A  J A I N

T R U E  L O V E 
1 1 0 0  0 1 0 0
   2       1        = 21%

   
Python is case-sensitive, so a and A would be different characters. Use the lower function ie

and the count function to count
"""
# Message Prompt
print("Love Calculator. See if you and your partner are compatible together")


# User Input
name1 = input("Enter your First and Last Name(First User): ")
name2 = input("Enter your First and Last Name(Second User): ")
lovescore = 0

name1_lower = name1.lower
name1_lower = name1.lower

# Using TRUE LOVE as the calculator
if ("t" in name1) or ("T" in name1):
    lovescore += 1
else:
    lovescore += 0

if ("r" in name1) or ("R" in name1):
    lovescore += 1
else:
    lovescore += 0

if ("u" in name1) or ("u" in name1):
    lovescore += 1
else:
    lovescore += 0

if ("e" in name1) or ("E" in name1):
    lovescore += 1
else:
    lovescore += 0

if ("l" in name1) or ("L" in name1):
    lovescore += 1
else:
    lovescore += 0

if ("o" in name1) or ("O" in name1):
    lovescore += 1
else:
    lovescore += 0

if ("v" in name1) or ("V" in name1):
    lovescore += 1
else:
    lovescore += 0

if ("e" in name1) or ("E" in name1):
    lovescore += 1
else:
    lovescore += 0

if ("t" in name2) or ("T" in name2):
    lovescore += 1
else:
    lovescore += 0

if ("r" in name2) or ("R" in name2):
    lovescore += 1
else:
    lovescore += 0

if ("u" in name2) or ("u" in name2):
    lovescore += 1
else:
    lovescore += 0

if ("e" in name2) or ("E" in name2):
    lovescore += 1
else:
    lovescore += 0

if ("l" in name2) or ("L" in name2):
    lovescore += 1
else:
    lovescore += 0

if ("o" in name2) or ("O" in name2):
    lovescore += 1
else:
    lovescore += 0

if ("v" in name2) or ("V" in name2):
    lovescore += 1
else:
    lovescore += 0

if ("e" in name2) or ("E" in name2):
    lovescore += 1
else:
    lovescore += 0

print(lovescore)