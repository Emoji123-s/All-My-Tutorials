"""
Hangman is a guessing game for two or more players. One player thinks of a word, phrase, or sentence and the other(s) tries to guess it by suggesting letters or numbers within a certain number of guesses.

The first player thinks of  a word, phrase or sentence (fruit, food, places, animals, etc)

Supposedly the first player thinks "apple". To the second player, it is shown as
                _ _ _ _ _ 
The second player has to guess the word by saying letters, but within a given number of guesses. A hangman figure consists of one head, 2 arms, 2 legs and one body, making 6 guesses, but this can be flexible as well.

Supposedly the second user chooses 'X'
                _ _ _ _ _ ('X' is wrong, so the first user draws the head)
Second guess = 'A'
                A _ _ _ _ ('A' is correct, so the figure stays the same, and no life is lost.)
Third guess = 'Y'
                A _ _ _ _ ('Y' is incorrect, so the first user draws one other part of the hangman, probably the body)
Fourth guess = 'Z'
                A _ _ _ _ ('Z' is incorrect, so the first user draws another part of the hangman, probably an arm)
Fifth guess = 'M'
                A _ _ _ _ ('M' is incorrect, so the first user draws another part of the hangman, another arm)
Sixth guess = 'E'
                A _ _ _ E ('E' is correct, so the figure stays the same)
Seventh guess = 'P'
                A P P _ E ('P' is correct, so the figure stays the same)
Eighth guess = 'B'
                A P P _ E ('B' is incorrect, so the first user draws another part of the hangman, one leg)
Ninth guess = 'C'
                A P P _ E ('C' is incorrect, so the first user draws another part of the hangman, another leg)

At this point, the second player loses, because the figure is hanged. If the word is completed, the second user wins. 

Input and prompt message
Let's Play Hangman!

You have only 6 lives to try and guess the word within 6 attempts! Good luck!!

['_', '_', '_', '_', '_', '_',]
Guess a letter :
Once the user inputs a letter, like "x"

Output:
You guessed x that is not present in the word. So you lose a life
['_', '_', '_', '_', '_', '_',]

    <--->
    |   |
    O   |
        |
        |
        |
==========
Guess a letter:
you lose
    <--->
    |   |
    O   |
   /|\  |  # type: ignore
   / \  | # type: ignore
        |
==========
"""

# Import libraries
import random

# Define the variable "words"

words = ["apple", "banana", "carrot", "durian", "eggplant", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "orange", "peach", "pineapple", "pineapple", "pineapple", "pineapple", "pineapple", "pineapple", "pineapple", "pineapple", "pineapple", "pineapple", "pineapple", "pine"]

# Generate a word
word = random.choice(words)

# Message prompt
print("Let's Play Hangman!")
print("Proper nouns, such as names, places, brands, or slangs are forbidden 😡")
print(f"You have only {len(word)} lives to try and guess the word within {len(word)} attempts! Good luck!!")

# initializing variables
underscore = "_"

# Initial Hangman display
hangman = """
  _______
 |       |
 |
 |
 |
 |
_|______
"""
print(hangman)

# Length of the word
length = len(word)

# Represent the chosen word with underscore

for i in range(length):
    underscore = underscore.replace(word[i], "_")

print(underscore)

# User input
guess = input("Guess a letter : ")
