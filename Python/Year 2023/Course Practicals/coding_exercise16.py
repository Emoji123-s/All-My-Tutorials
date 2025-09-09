"""
Program to calculate the sum of even numbers from 1-100, including 1 and 100
"""

result = 0

for i in range(2, 101, 2):
    result += i
print(result)