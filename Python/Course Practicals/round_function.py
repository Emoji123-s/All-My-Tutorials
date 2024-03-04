"""
The round function is used to round off numbers. The general syntax is
                round(number to be rounded, number of digits)
The number of digits is optional, which can be positive or negative, and the maximum number of decimal points is 2. If the number of digits isn't passed, it is considered as 0 by default
"""
print(round(21.333333333)) # 21, because there is no argument affecting it
print(round(21.333333333, 2)) # 21.33, because it's rounding to 2 decimal place
print(round(21.333333333, -2)) # 0.0, because it's rounding the first 2 figures to zero
print(round(7)) # 7, because the nearest decimal digit to 7 is 7, and there is no argument affecting it
print(round(7,2)) # 7, because it is still a whole number, so nothing would be rounded
print(round(7.61)) # 8, because it immediately considers it as zero, so it prints the rounded number
print(round(2.6666, 2)) # 2.67, because it's rounding to 2 decimal place
print(round(2.6657, 0)) # 3.0, because its only printing out whole numbers, and there is no argument affecting it
# If there are numbers to a decimal place, and you provide an end digit of zero(0) to round them, then it prints as a float. If you don't provide an end digit, then it will return as an integer

# Special Cases
# With this, 2 cases can be found. It can return the nearest even number, or the odd number, but even is most preferred
print(round(7.5)) # 8, because you can round 5 to a +1, so it'll print 8 as an integer
print(round(6.5)) #6, even though this would ordinarily be 7, but it prints the nearest even number, and 6 is an even number nearest to 6
print(round(11.5)) # 12, because 12 is the nearest even number next to 11
print(round(12.5)) # 12, because 12 is the nearest even number next to 12

# Rounding Integers
"""
If a negative number is provided to an integer, then it returns the multiple of the number closest to the multiple of 10^(-number of digits) i.e
                10^-(-1)
                = 10^(1)
                = 10
"""
print(round(674, 2)) # It wil directly return 674, because it doesn't affect positive values
print(round(674, 0)) # Also prints 674
print(round(674, -2)) # The nearest multiples of 10 is 670 and 680, so since 674 is closest to 670, 670 will be printed. 
print(round(674, -3)) # This will print 1000,because the closest multiple of 674 to 000 is 1000
print(round(674, -4)) # This will print out zero, because it exceeds.
print(round(665, -1))
print(round(675, -1))
print(round(-8/3))
print(round(6.75, 1))
print(round(6.85, 1))
print(round(674.1012, -1))
print(round(1212, -2))
print(round(467, -3))