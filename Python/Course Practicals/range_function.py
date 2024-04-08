"""
Syntax

                    range(start,stop,step size)
Start : 
    It means the starting point for the number series, and it is completely optional

Stop : 
    It means where to stop, and it is completely mandatory

Step Size : 
    By default, step size is 1, and it is completely optional. For example
                    range(2,6,2) - This will start printing from 2, skip the number 3, and print 4. Since the range stops at 6, it'll skip 5 and stop printing

In a for loop:
                    for var_name in range(i,j,k):
                        statement(s)
"""
# Using Indexes
a = range(5)
print(a[0])

# In a for loop
for i in a:
    print(i)

# Add numbers from 1-100 and print the result
total = 0
for num in range(1,101):
    total += num
print(total)