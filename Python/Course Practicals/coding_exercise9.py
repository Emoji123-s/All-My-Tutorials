"""
Write an automatic pizza program. Determine the final bill according to the user's input
Small Pizza = 1000
Medium Pizza = 2000
Large Pizza = 3000

Pepperoni for small pizza = 300
Pepperoni for medium and large pizza = 500

Extra cheese for any size = 200
"""
# User input and prompt message

print("Automatic Pizza Program")
name = input("Enter your name : ")
print (f"Hello {name}, Let's Make you a Pizza!")

types = """
1 = Small Pizza = 1000
2 = Medium Pizza = 2000
3 = Large Pizza = 3000
"""
print(types)
smallpizza = 1000
mediumpizza = 2000
largepizza = 3000
peppe_smallpizza = 300
peppe_medpizza = 500
peppe_largepizza = 500
extracheese = 200
pizza_size = int(input("What pizza size are you getting? "))

# User Conditions
if (pizza_size == 1):
    print("Creating Small Pizza....")
    print("Small Pizza is 1000 Naira")
    format1 = """
    Pepperoni for small pizza = 300 Naira
    """
    print(format1)
    pepperoni = input("Do you want Pepperoni? Yes/No: ")
    if (pepperoni == "Yes" or pepperoni == "yes"):
        print("Pepperoni Added")
        print("Creating Small Pizza.....")

        format2 = """
        Extra cheese for any size = 200 Naira
        """
        cheese = input("Do you want extra cheese? Yes/No: ")
        if (cheese == "Yes" or cheese == "yes"):
            print("Extra Cheese Added")
            print(f"Pizza Creation Complete. Your total balance is {smallpizza + peppe_smallpizza + extracheese} Naira. Please proceed to the counter to pay")
        if (cheese == "No" or cheese == "no"):
            print(f"Pizza Creation Complete. Your total balance is {smallpizza + peppe_smallpizza} Naira. Please proceed to the counter to pay")
    if (pepperoni == "No" or pepperoni == "no"):
        print("Creating Small Pizza....")
        format2 = """
        Extra cheese for any size = 200 Naira
        """
        cheese = input("Do you want extra cheese? Yes/No: ")
        if (cheese == "Yes" or cheese == "yes"):
            print("Extra Cheese Added")
            print(f"Pizza Creation Complete. Your total balance is {smallpizza  + extracheese} Naira. Please proceed to the counter to pay")
        if (cheese == "No" or cheese == "no"):
            print(f"Pizza Creation Complete. Your total balance is {smallpizza} Naira. Please proceed to the counter to pay")

elif (pizza_size == 2):
    print("Creating Medium Pizza....")
    print("Medium Pizza is 2000 Naira")
    format1 = """
    Pepperoni for medium and large pizza = 500 Naira
    """
    print(format1)
    pepperoni = input("Do you want Pepperoni? Yes/No: ")
    if (pepperoni == "Yes" or pepperoni == "yes"):
        print("Pepperoni Added")
        print("Creating Medium Pizza.....")

        format2 = """
        Extra cheese for any size = 200 Naira
        """
        cheese = input("Do you want extra cheese? Yes/No: ")
        if (cheese == "Yes" or cheese == "yes"):
            print("Extra Cheese Added")
            print(f"Pizza Creation Complete. Your total balance is {mediumpizza + peppe_medpizza + extracheese} Naira. Please proceed to the counter to pay")
        if (cheese == "No" or cheese == "no"):
            print(f"Pizza Creation Complete. Your total balance is {mediumpizza + peppe_medpizza} Naira. Please proceed to the counter to pay")
    if (pepperoni == "No" or pepperoni == "no"):
        print("Creating Medium Pizza....")
        format2 = """
        Extra cheese for any size = 200 Naira
        """
        cheese = input("Do you want extra cheese? Yes/No: ")
        if (cheese == "Yes" or cheese == "yes"):
            print("Extra Cheese Added")
            print(f"Pizza Creation Complete. Your total balance is {mediumpizza  + extracheese} Naira. Please proceed to the counter to pay")
        if (cheese == "No" or cheese == "no"):
            print(f"Pizza Creation Complete. Your total balance is {mediumpizza} Naira. Please proceed to the counter to pay")

elif (pizza_size == 3):
    print("Creating Large Pizza....")
    print("Large Pizza is 3000 Naira")
    format1 = """
    Pepperoni for medium and large pizza = 500 Naira
    """
    print(format1)
    pepperoni = input("Do you want Pepperoni? Yes/No: ")
    if (pepperoni == "Yes" or pepperoni == "yes"):
        print("Pepperoni Added")
        print("Creating Large Pizza.....")

        format2 = """
        Extra cheese for any size = 200 Naira
        """
        cheese = input("Do you want extra cheese? Yes/No: ")
        if (cheese == "Yes" or cheese == "yes"):
            print("Extra Cheese Added")
            print(f"Pizza Creation Complete. Your total balance is {largepizza + peppe_largepizza + extracheese} Naira. Please proceed to the counter to pay")
        if (cheese == "No" or cheese == "no"):
            print(f"Pizza Creation Complete. Your total balance is {largepizza + peppe_largepizza} Naira. Please proceed to the counter to pay")
    if (pepperoni == "No" or pepperoni == "no"):
        print("Creating Large Pizza....")
        format2 = """
        Extra cheese for any size = 200 Naira
        """
        cheese = input("Do you want extra cheese? Yes/No: ")
        if (cheese == "Yes" or cheese == "yes"):
            print("Extra Cheese Added")
            print(f"Pizza Creation Complete. Your total balance is {largepizza  + extracheese} Naira. Please proceed to the counter to pay")
        if (cheese == "No" or cheese == "no"):
            print(f"Pizza Creation Complete. Your total balance is {largepizza} Naira. Please proceed to the counter to pay")
else:
    print("Not a reoognized value")