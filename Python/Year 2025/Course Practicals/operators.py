# Operators

"""
They are simply symbols or operators that are used to perform functions in Python. For example

                                        5 + 2
                                5,2 = Operands
                                + = Operator

Aritmetic Operators
+ = Plus/Addition
- = Minus/Subtraction
* = Times/Multiplication
/ = Division (Outputs in float)
% = Modulus/Remainder
// = Floor Division (changes from float to integer)
** = Power


PEMDAS
- Parenthesis, Exponents, Multiplication/Division, Addition/Subtraction. 
print(5 + 2) # Addition
print(5 - 2) # Subtraction
print(5 * 2) # Multiplication
print(5 / 2) # Division
print(5 % 2) # Modulus, prints the remainder, in thsis case, 1, because 2 goes into 5 twice, with 1 remaining.
print(5 // 2) # Floor Division
print(5 ** 2) # Exponentiation
print(5 + 2 * 3) # Multiplication first, then addition
print((5 + 2) * 3) # Parenthesis first, then multiplication

shorthand assignment operators include:
+=
-=
*=
/=
%=
//=
**=
For example:
a = 5
a += 2 # This is the same as a = a + 2
print(a) # This will print 7
You can also do more than one assignment at a time:
a,b = 5,4
print(a) # This will print 5
print(b) # This will print 4

"""

"""
Comparison Operators
== Equal to
!= Not equal to
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to

In comparison operators, there must be a container to compare, for example:
print(5 == 2) # Equal to
print(5 != 2) # Not equal to
print(5 > 2) # Greater than
print(5 < 2) # Less than
print(5 >= 2) # Greater than or equal to
print(5 <= 2) # Less than or equal to

Doing 5 == a will give an error, because there is no container to compare 5 to.

It will return a boolean value, either True or False, depending on the comparison.

"""

"""
Logical Operators
They are used to combine conditional statements.
AND
                        Truth Table for AND
                        True    True    True
                        True    False   False
                        False   True    False
                        False   False   False
OR
                        Truth Table for OR
                        True    True    True
                        True    False   True
                        False   True    True
                        False   False   False
NOT
                        Truth Table for NOT
                        True    False
                        False   True    

For example:
print(5 > 2 and 5 < 10) # AND, both conditions must be true. If one is false, it will return False
print(5 > 2 or 5 < 1) # OR, at least one condition must be true. If one is false, it will return True.
print(not(5 > 2)) # NOT, reverses the result, in this case it will return False
"""