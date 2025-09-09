"""
Break : 
It can only be used within a for and while loop, and it exits from the loop immediately.

Syntax
                        for loop:
                            # Code
                            if condition:
                                break;
                            # More Code
                        Outside of loop
"""


"""
While Loop
count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 7:
        break
    print("Hi")
print("Out of while loop")


# Nested loop
list1 = ["hi", "hello", "welcome"]
list2 = ["Davina", "Damien", "Dracula"]

for item in list1:
    for name in list2:
        print(item, name)
        if item == "hello" and name == "Damien":
            break
        print("Out from inner loop")
print("Out of for loop")
"""

"""
Continue : 
This is the opposite of break statement, as it continues with the next iteration in the program. 

Syntax
                    for loop / while loop:
                        # code
                        if condition:
                            continue
                        # more code
                    # Out of loop

# While
count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 7:
        continue
    print("Hi")
print("Out of while loop")

# For
for i in range(1, 11):
    if i == 7:
        continue
    else:
        print(i)
"""

"""
Pass : 
It is used to define an empty function or loop. It acts like a placeholder for statements and loops that are not currently defined, but will be defined as time goes on. Basically to ignore a part of code or function. 
"""
for i in range(1, 11):
    pass