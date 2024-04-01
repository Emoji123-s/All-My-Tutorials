"""
                                        Problem Statement
Rules:  Rock wins against Scissors
        Scissors wins against Paper
        Paper wins against Rock

The user is going to play against the computer. User input would be choices implemented based on the numbers below

Supposedly
        0 = Rock
        1 = Paper
        2 = Scissors

The computer will generate a random number and choose from the list of options above between 0 to 2, and check the numbers that the user and the computer has chosen, and tell who won and who lost

If there are a total number of 9 cases i.e, user's choice and computer choice

    0,1,2                       0,1,2
Users Choice            Computer's Choice
    0                           0  = Draw
    0                           1  = Computer
    0                           2  = User

    1                           0  = User
    1                           1  = Draw
    1                           2  = Computer

    2                           0  = Computer
    2                           1  = Draw
    2                           2  = User

With this, add if-else statements/elif statements. 
If the computer and user choice is the same, it's a draw. (For 0 0, 1 1, 2 2)
If user choice is zero and computer choice is one, paper will in against rock (computer wins). 
If user choice is zero and computer choice is two, rock will win against scissors (user wins)
If user choice is one and computer choice is zero, paper will win against rock (user wins)
If user choice is one and computer choice is two, scissors will win against paper (computer wins)
If user choice is two and computer choice is zero, rock will win against scissors (computer wins)
If user choice is two and computer choice is one, scissors will win against paper (user wins)

Trying in an if/else statement. The order matters when putting the conditions matter. Think through it

if (computer_choice > user_choice):
    print("You Lose")  = This covers cases 0 1, and 1 2

elif (user_choice > computer_choice):
    print("You Win")  = This covers cases 1 0, and 2 1

if (computer_choice == user_choice):
    print("It's a draw")  = This covers cases 0 0, 1 1 and 1 2

if (user_choice == 0 and computer_choice == 2):
    print("You Win")  = This covers cases 0 2

if (user_choice == 2 and computer_choice == 0):
    print("You Lose")  = This covers cases 2 0

else:
    print("Wrong Value, Try again)
"""

# Message Prompt
print("Rock, Paper, Scissors")
print("Select a value ranging from 0 - 2. 0 = Rock, 1 = Paper, 2 = Scissors")