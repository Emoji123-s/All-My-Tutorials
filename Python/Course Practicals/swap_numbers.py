# program to swap 2 numbers

print("Welcome to your Number Swapper :)")
print("Input your selected numbers below")
# First, let's take the input from the user

a = input("Enter your number for a: ")
b = input("Enter your number for b: ")

# To swap, we would need a third container/variable, and our input should be a=value of b, and b= value of a
#Let's try adding a third variable
# since a=value of b, and b=value of a
c = a
a = b
b = c

print("a =" + " " + a)
print("b =" + " " + b)

print("Cool, innit? :D")