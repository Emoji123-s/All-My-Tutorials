"""
It is a module that aids randomization. It is used to generate pseudo-random numbers, because they are not truly random, they are deterministic. All you need is to import the module into the program
"""

import random

# Functions
"""
randint(a, b) - Returns a number between a and b i.e, (a <= X <= b) (Both a and b are inclusive)

randrange(a, b) - Returns a number between a and b i.e, (a <= X < b) (Only a is inclusive)

random() - Returns a floating point number. By default, the range will be (0.0 <= X < 1.0) (Numbers reaching 0.99999999, but never a 1.0)

uniform() - Returns a floating point number, but for a particular range

choice() - To select a random item from a sequence

shuffle() - To shuffle through a sequence
"""
a = random.randint(1, 3) # Returns an integer between 1 and 3, but 1 and 3 are included
print(a)

b = random.randrange(1, 3) # Here, you can get 1 and 2 only. 3 is not included
print(b)

c = random.random() # Returns a floating point, but 1.0 is not included
print(c)

d = random.uniform(1, 3) # Returns a float number in a range
print(d)

# Taking a list
mylist = [1, 2, 3, 4, 5, 6]
# From this list, I want a random number
e = random.choice(mylist) # Picks out a number from a list everytime it runs
print(e)

# What if we want to shuffle
random.shuffle(mylist) # Shuffles the list everytime it runs
print(mylist)