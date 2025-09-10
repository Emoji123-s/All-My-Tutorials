# Errors in Python

# Syntax Error
#print("Hello World"  # Uncommenting this line will cause a syntax error

#indentation Error
def example_function():
    print("This line is correctly indented")
    # Uncommenting the next line will cause an indentation error
#print("This line is incorrectly indented")
    print("This line is also correctly indented")
    #print("This line is incorrectly indented")
    print("End of function")
example_function()
# Name Error
#print(undeclared_variable)  # Uncommenting this line will cause a name error

# Type Error
#print("Hello" + 5)  # Uncommenting this line will cause a type error

# Value Error
#print(int("Hello"))  # Uncommenting this line will cause a value error

# Index Error
my_list = [1, 2, 3]
#print(my_list[5])  # Uncommenting this line will cause an index error

# Key Error
my_dict = {"a": 1, "b": 2}
#print(my_dict["c"])  # Uncommenting this line will cause a key error

# Attribute Error
my_string = "Hello"
#print(my_string.non_existent_method())  # Uncommenting this line will cause an attribute error

# Zero Division Error
#print(10 / 0)  # Uncommenting this line will cause a zero division error

# Import Error
#import non_existent_module  # Uncommenting this line will cause an import error

# Module Not Found Error
#from non_existent_module import non_existent_function  # Uncommenting this line will cause a
# module not found error

# File Not Found Error
#with open("non_existent_file.txt", "r") as file:  # Uncommenting this line will cause a file not found error
#    content = file.read()
#    print(content)

# IOError
#with open("/root/secret_file.txt", "r") as file:  # Uncommenting this line will cause an IOError
#    content = file.read()
#    print(content)
