# Arithmetic Operators
"""
print(5+2)  Addition operator, prints as an integer
print(5-2)  Subtraction operator, prints as an integer
print(5/2)  Division operator, prints as a float
print(5*2)  Multiplication operator, prints as an integer
print(5**2) Exponentation operator, prints as an integer
print(5%2)  Modulo operator, prints as an integer
print(5//2) Floor Division operator, prints as an integer. The floor division is used to convert a float operand to an integer value. If for some reason we have a decimal value, the floor divisio converts this into an integer, without the decimal value 


# According to PEMDAS (Precedence and Associativity)

Parentheses ()
Exponentation ** (Right to left)
Multiplication *, Division /, Floor Division //, Modulo % (Left to right)
Addition +, Subtraction -, (Left to right)


# Taking an example

print(5+2*3-1+10/5) # This gives a float number, because of the division. If we switch that to a floor division operator
print(5+2*3-1+10//5) # This gives us an integer number.


# Assignment and Comparison Operators

# Assignment Operators 
# The following are shorthand assignment operators

+= - Addition i.e, a += 5 (a = a + 5)
-= - Subtraction i.e, a -= 5 (a = a - 5)
*= - Multiplication i.e, a *= 5 (a = a * 5)
/= - Division i.e, a /= 5 (a = a / 5)
//= - Floor Division i.e, a //= 5 (a = a // 5)
%= - Modulo i.e, a %= 5 (a = a % 5)
**= - Exponentation i.e, a **= 5 (a = a ** 5)


a,b = 4,3
c = a+b
a+=2
c += a
print(c)
# Comparison Operators
# The following are comparison operators

> - Greater than
< - Less than
>= - Greater than or equal to
<= - Less then or equal to
== - Double equal to
!= - Not equal to

a = 5
print(a < 5)
print(a == 5)


# Logical Operators
# The following are logical operators

and - If both of the statements are true, then and prints true. If one of the statements is true, and prints false
or - If one of the statements is true, then the result is true
not - It reverses the result of a given statement. So if a statement is true, not prints false, and vice versa


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
c,d = 6,7

print(c & d) # First the numbers get converted to their binary form, stored in either a 4 or 8-bit format, then bitwise and is performed
print(c | d)
print(~c)
print(~b)
print(c ^ d)
print(c >> d)
print(c << d) 
"""

# Identity Operators
"""
They are used to compare objects if they are the same or not, as well as if they share the same memory location. There are 2 types:
is
is not
"""
e = 5
f = 5
print(e is f)
# In python, the memory manager resues the object instead of allocating new memory for the same data and datatype. So in this case, b will be linked to the memory address of a, and a and be can be accessed. So basically, identity operator compares the MEMORY ADDRESS of objects. So basically
print(e == f) # This should print true as well, because now it is comparing the values.
# To check the id of an object,
print(id(e))
print(id(f)) # They both have the same id. You can do it with the values as well

# if we have
g = 6
h = "6"
print(g is h) # This should return false, because the datatypes are not the same
print(id(g))
print(id(h))

# is not
print(g is not h) # This should print true, because g is not the same datatype as h, therefore they have different memory locations. It is basically the reverse of the "is" operator.
print(e is not f) # This will print false, because the memory location are the same, so it'll reverse the operation and print true.
print(id(e) == id(f)) # Here, we are comparing the address of the variable e and f. It also means print(e is f)

i = 10
print(id(i))

print(i is i)

# Membership Operators
"""
There are 2 operators
in
not in
"""
word = "Divine"
print("y" in word)
print("d" in "Divine") # Membership operators are case-sensitive, so this would print false, even thoigh there is a capital letter D in the string sequence
print("d" not in word) # This will return true, because "d" is not in the string sequence
print("D" not in word) # This will return false, because it is in the string sequence

# Let's try it in a list
li_st = [1, 10, -1, 0, 17]
print(10 in li_st) # This should return true, because 10 is in the list
print(10 not in li_st) # This should return false, because 10 is in the list
print(20 not in li_st) # This should return true, because 20 is not in the list
print(20 in li_st) # This should print false, because 20 is not in the list