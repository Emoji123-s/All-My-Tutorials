"""
FizzBuzz Job Interview Question. Write a program that prints 1-n (n can be anything,but today 100), but the numbers which are divisible by 3 should print 3, the numbers divisible by 5 should print buzz, and the number divisible by both 3 and 5 should print FizzBuzz. Every other thing should print the numbers
"""

# Using For loop
for i in range(1,101):
    if (i % 3) == 0 and (i % 5) == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) 