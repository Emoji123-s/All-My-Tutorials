"""
Syntax
                    for var_name in sequence:
                        statement(s)
                    else:
                        statement(s)
The else block will be executed only if the for loop has completed successfully

If we have a list
                numbers = [2,3,4,5,6,7,8,9]
we can use a for loop to traverse through the list
                for i in numbers:
                    print(i)
                else:
                    print("Successfully completed!")
"""
# Using tuples 
tuple1 = (2, 50, 6, 34, 5, -1)
for i in tuple1:
    print(i)
    #if i == 5:
       # break  with this, we won't get an else statement because we broke out of the loop
else:
    print("Loop Successfully completed")
