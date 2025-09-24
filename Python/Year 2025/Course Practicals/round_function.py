# Round Function

""""
General syntax: round(number, ndigits)
It basically rounds a number to a given precision in decimal digits (default 0 digits). For example:
print(round(5.76543, 2)) # it will return 5.77
print(round(5.76543, 3)) # it will return 5.765
print(round(5.76543)) # it will return 6
print(round(5.76543, 0)) # it will return 6

Generally, the round function rounds to the nearest even number when the number is exactly halfway between two integers. This is called bankers rounding. or tied rounding. For example:
print(round(2.5)) # it will return 2
print(round(3.5)) # it will return 4

Providing a negative value for ndigits will round to the left of the decimal point. It basically rounds that number off to the nearest multiple of 10^(-ndigits). For example: 
print(round(674, -1)) # it will return 670, because the closest multiple of 10 is 670, essentially turning the last digit to 0 and the rounding off the second digit with respect to the last digit.
print(round(674, -2)) # it will return 700, because the closest multiple of 100 is 700, essentially turning the last two digits to 0 and the rounding off the first digit with respect to the second digit.
Using the formula itself:
print(round(674, -1)) # it will return 670, because 674/10 = 67.4, which rounds to 67, and then multiplying by 10 gives 670.
print(round(674, -2)) # it will return 700, because 674/100 = 6.74, which rounds to 7, and then multiplying by 100 gives 700.
print(round(675, -3)) # it will return 1000, because 675/1000 = 0.675, which rounds to 1, and then multiplying by 1000 gives 1000.

We can round off negative numbers as well. For example:
print(round(-2.5)) # it will return -2, because -2 is the nearest even number.
print(round(-3.5)) # it will return -4, because -4 is the nearest even number.
"""