# Arithmetic Operators
"""
print(5+2)  Addition operator, prints as an integer
print(5-2)  Subtraction operator, prints as an integer
print(5/2)  Division operator, prints as a float
print(5*2)  Multiplication operator, prints as an integer
print(5**2) Exponentation operator, prints as an integer
print(5%2)  Modulo operator, prints as an integer
print(5//2) Floor Division operator, prints as an integer. The floor division is used to convert a float operand to an integer value. If for some reason we have a decimal value, the floor divisio converts this into an integer, without the decimal value 
"""

# According to PEMDAS (Precedence and Associativity)
"""
Parentheses ()
Exponentation ** (Right to left)
Multiplication *, Division /, Floor Division //, Modulo % (Left to right)
Addition +, Subtraction -, (Left to right)
"""

# Taking an example
"""
print(5+2*3-1+10/5) # This gives a float number, because of the division. If we switch that to a floor division operator
print(5+2*3-1+10//5) # This gives us an integer number.
"""

"""
5th project to learn Arithmetic operators. Calculate BMI (Body Mass Index) i.e, weight / height**2. Take a weight in kg from the user(int), and height in metres as a float value.

weight = int(input("Enter your weight (In kg, numbers only): "))
height = float(input("Enter your height (In metres, numbers only): "))

# To calculate the BMI, the formula is
bmi = weight / (height**2)

# Since exponentation has a higher precedence,
print("Your BMI (Body Mass Index) is " + str(bmi))

"""
# Assignment and Comparison Operators

# Assignment Operators 
# The following are shorthand assignment operators
"""
+= - Addition i.e, a += 5 (a = a + 5)
-= - Subtraction i.e, a -= 5 (a = a - 5)
*= - Multiplication i.e, a *= 5 (a = a * 5)
/= - Division i.e, a /= 5 (a = a / 5)
//= - Floor Division i.e, a //= 5 (a = a // 5)
%= - Modulo i.e, a %= 5 (a = a % 5)
**= - Exponentation i.e, a **= 5 (a = a ** 5)
"""

a,b = 4,3
c = a+b
a+=2
c += a
print(c)
# Comparison Operators
# The following are comparison operators
"""
> - Greater than
< - Less than
>= - Greater than or equal to
<= - Less then or equal to
== - Double equal to
!= - Not equal to
"""
a = 5
print(a < 5)
print(a == 5)


# Logical Operators
# The following are logical operators
"""
and - If both of the statements are true, then and prints true. If one of the statements is true, and prints false
or - If one of the statements is true, then the result is true
not - It reverses the result of a given statement. So if a statement is true, not prints false, and vice versa
"""

# For and
a,b = 5,4
print(a>4 and b<10)
print(a>4 and b>10)

# For or
print(a>4 or b<10)
print(a>4 or b>10)

# For not
print(a>4)
print(not(a))


# Bitwise Operators
# The following are bitwise operators
"""
& - bitwise and - If both value is 1, the result is 1
| - bitwise or - If a value is 1, the result is one
^ - bitwise xor - If both values are 1, the result is zero
~ - not / complement - reverses the bit into a negative value, i.e, ~5 = -6. We can't store a negative answer in menory, so we use 2's complement, and the formula is
                    2's = 1's + 1
                    where 1's = reversing of the positive bits of the not result
<< - left shift - This operator gains bit by shifting the bits of a number to the left. The simple way is this
                    x * 2^n
                    where x = number to be shifted
                          n = bits to be added
>> - right shift - This operator loses bit by shifting the bits of a number to the right. The simple way is this
                    x / 2^n
                    where x = number to be shifted
                          n = bits to be added

The bitwise operators as the name suggests works on bits. So if we have
""" 
c,d = 6,7

print(c & d) # First the numbers get converted to their binary form, stored in either a 4 or 8-bit format, then bitwise and is performed
print(c | d)
print(~c)
print(~b)
print(c ^ d)
print(c >> d)
print(c << d) 