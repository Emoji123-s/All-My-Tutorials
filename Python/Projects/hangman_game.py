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

import random

# Define the variable "words"
words = ["apple", "banana", "carrot", "durian", "eggplant", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "orange", "peach", "pineapple"]

# Generate a word
word = random.choice(words)

# Length of the word
word_length = len(word)

# Message prompt
print("Let's Play Hangman!")
print("Proper nouns, such as names, places, brands, or slangs are forbidden 😡")
print(f"You have only 6 lives to try and guess the word within 6 attempts! Good luck!!")

# initializing underscore variable
display = ""

# Getting the underscore
for letters in range(word_length):
    display += "_"

# Initial Hangman display
hangman_stages = [
    """
  _______
 |       |
 |
 |
 |
 |
_|______
""",
    """
  _______
 |       |
 |       O
 |
 |
 |
_|______
""",
    """
  _______
 |       |
 |       O
 |       |
 |
 |
_|______
""",
    """
  _______
 |       |
 |       O
 |      /|
 |
 |
_|______
""",
    """
  _______
 |       |
 |       O
 |      /|\\
 |
 |
_|______
""",
    """
  _______
 |       |
 |       O
 |      /|\\
 |      /
 |
_|______
""",
    """
  _______
 |       |
 |       O
 |      /|\\
 |      / \\
 |
_|______
"""
]

# initializing variable to hold a boolean to flip, and the lives the user has
game_over = False
lives = 6

# Using while loop
while not game_over:
    # Display Hangman figure
    print("Hangman:")
    print(hangman_stages[6 - lives])
    print(display)
    guess = input("Guess a letter: ")
    # Checking if the guess is in the word
    if guess in word:
        print(f"You guessed {guess} that is present in the word.")
        # Updating the display
        for position in range(word_length):
            letter = word[position]
            if letter == guess:
                display = display[:position] + letter + display[position + 1:]
        print(f"You have {lives} lives left")
    else:
        print(f"You guessed {guess} that is not present in the word. So you lose a life")
        lives -= 1
        print(f"You have {lives} lives left")
    # Checking if the user has lost
    if lives == 0:
        game_over = True
        print("You lose")
        print(f"The word was {word}")
    # Checking if the user has won
    if "_" not in display:
        game_over = True
        print("You win")
        print(f"The word was {word}")
