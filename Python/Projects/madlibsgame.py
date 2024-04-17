# Mad Libs is a phrasal template word game created by Leonard Stern and Roger Price. It consists of one player prompting others for a list of words to substitute for blanks in a story before reading aloud. The game is frequently played as a party game or as a pastime.

# Welcome message
from os import replace


print("Welcome to Mad Libs..... :D")
print("In this game, a set of adjectives, nouns and verbs would be asked of you to input before revealing your story. Let's Play :)")

# Multi-comment to hold the story template

story = """
Once upon a time, in a [adjective1] [noun1], there lived a [adjective2] [noun2].
One day, the [noun2] decided to [verb1] to the [place].
On the way, the [noun2] met a [adjective3] [noun3] who offered some [noun4].
After [verb2] for hours, they finally reached the [place] and [verb2] happily ever after.
"""

# Variables to hold the user's input(10)
adjective1 = input("Enter your first adjective: ")
noun1 = input("Enter your first noun: ")
adjective2 = input("Enter your second adjective: ")
noun2 = input("Enter your second noun: ")
verb1 = input("Enter your first verb: ")
place = input("Enter your first place: ")
noun3 = input("Enter your third noun: ")
adjective3 = input("Enter a third adjective: ")
verb2 = input("Enter a second verb: ")
noun4 = input("Enter your fourth noun: ")

# Filling in the blanks, using subscript to pick out selected words
# The .replace is a python method used to replace one substring with another substring
filled = story.replace("[adjective1]", adjective1)\
              .replace("[noun1]", noun1)\
              .replace("[adjective2]", adjective2)\
              .replace("[noun2]", noun2)\
              .replace("[verb1]", verb1)\
              .replace("[place]", place)\
              .replace("[noun3]", noun3)\
              .replace("[adjective3]", adjective3)\
              .replace("[verb2]", verb2)\
              .replace("[noun4]", noun4)
# So cool, by the way..... :))
# Now the user can see their story, however they chose their parts of speech
print("Here's your completed story :) \n")
print(filled)