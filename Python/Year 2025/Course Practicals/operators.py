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

"""
Bitwise Operators
They are used to compare binary numbers. They include:
& = AND
| = OR
^ = XOR
~ = NOT
<< = Zero fill left shift
>> = Signed right shift

For example:
a = 5
b = 4
print(a & b) # AND, it will return 4, because 5 in binary is 101 and 4 is 100, and only the last digit is the same. When converting, if both digits are 1, it will return 1, otherwise it will return 0.

print(a | b) # OR, it will return 5, because 5 in binary is 101 and 4 is 100, and only the last digit is the same. When converting, if either digit is 1, it will return 1, otherwise it will return 0.

print(a ^ b) # XOR, it will return 1, because 5 in binary is 101 and 4 is 100, and only the last digit is different. When converting, if the digits are different, it will return 1, otherwise it will return 0.

print(~a) # NOT, it will return -6, because it inverts all the bits and adds 1 to the result. If it is 0, it will return 1, and if it is 1, it will return 0. Now, we cannot store negative number, so we use two's complement to store negative numbers. To get the two's complement, we invert all the bits and add 1 to the result. Basically
                                2's = 1's + 1( Two's complement is equal to one's complement plus one)
How to calculate one's complement:
                                5 = 0000 0101 (in binary)
                                ~5 = 1111 1010 (in binary)
To get two's complement, we add 1 to the result:
                                ~5 = 1111 1010
                                   +         1
                                ------------
                                -6 = 1111 1011 (in binary)
So if we have, probably ~10, it will be -11
If we have ~100, it will be -101. 

print(a << 2) # Zero fill left shift, it will left shift the first operand with respect to the number of bits specified in the second operand. In this case, it will return 20, because 5 in binary is 101, and when we left shift it by 2 bits, we add zeros to the left. So we get 10100, which is 20 in decimal. It's basically multiplying the number by 2 for each shift to the left. So, 5 * 2 * 2 = 20. 
if we have print(a << 3), it will return 40, because 5 * 2 * 2 * 2 = 40.
if we have print(a << 4), it will return 80, because 5 * 2 * 2 * 2 * 2 = 80.
if we have print(a << 5), it will return 160, because 5 * 2 * 2 * 2 * 2 * 2 = 160.

print(a >> 2) # Signed right shift, it will right shift the first operand with respect to the number of bits specified in the second operand. In this case, it will return 1, because 5 in binary is 101, and when we right shift it by 2 bits, we remove the last two bits. So we get 1, which is 1 in decimal. It's basically dividing the number by 2 for each shift to the right. So, 5 / 2 / 2 = 1. 
if we have print(a >> 3), it will return 0, because 5 / 2 / 2 / 2 = 0.
"""

"""
Identity Operators
They are used to compare objects if they are the same or not, as well as if they share the same memory location. There are 2 types:
is
is not

For example:
a = ["apple", "banana"]
b = a
print(a is b) # True, because a and b share the same memory location
print(a is not b) # False, because a and b share the same memory location
In identity operators, the memory manager reuses the same memory location for the same object to save memory. It doesn't create a new memory location for the same object. For example:
a = ["apple", "banana"]
b = ["apple", "banana"]
print(a is b) # False, because a and b do not share the same memory location, even though they have the same content.
To check the id of the object, we can use the id() function:
print(id(a)) # This will print the memory location of a

The difference between 'is' and '==':
is is used to check if the objects are the same, while == is used to check if the objects have the same value.
print(a == b) # True, because a and b have the same value
print(a is b) # False, because a and b do not share the same memory location
"""
