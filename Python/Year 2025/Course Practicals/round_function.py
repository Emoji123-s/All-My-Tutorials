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
"""
print(round(11.5))