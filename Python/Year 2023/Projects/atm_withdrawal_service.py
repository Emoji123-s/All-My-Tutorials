# Import libraries
import time 
import os

# Getting the variable pin

pin = os.getenv("PIN")


# Assuming the user has slotted in their card. Display Message Prompt
print("ATM Withdrawal.")
time.sleep(2)
print("Insert your card")
time.sleep(2)

# Display "Please Wait" with a wait time
print("Please Wait....")

# Using the time import to wait for 4 seconds to mimic the loading time of the machine to process
time.sleep(4)

# Adding a condition to limit password input
tries = 3

# Using while loop to loop the program until the user selects "no" at the end of the transaction
while tries > 0:
    # Request pin
    user_pin = (input("Enter your PIN : "))

    # Condition
    if (user_pin != pin):
        print("Access Denied")
        tries -= 1
        print(f"You have {tries} tries left")



    else:
        time.sleep(2)
        print("Select your Service from the list")
        print("1. Recharge")
        print("2. Balance Enquiry")
        print("3. Cash Withdrawal")
        print("4. Cash Deposit")
        print("5. Change PIN")
        print("6. Exit")

        # User input fot withdrawal
        user_choice = int(input())

        # For withdrawal
        time.sleep(1)
        if (user_choice == 3):
            print("1. Current")
            print("2. Savings")
            print("3. Joint")
            print("4. Zero")

            # If user choice is current
            user_choice = int(input())
            if (user_choice == 1):
                time.sleep(1)
                print("Do you want a receipt for this transaction? ")
                print("1. Yes")
                print("2. No")
                user_choice = int(input())
                if (user_choice == 1):
                    print("Sorry, Receipts are not available at this time")
                    time.sleep(1)
                    print("Enter an amount")
                    print("1. 1000")
                    print("2. 2000")
                    print("3. 3000")
                    print("4. 4000")
                    print("5. 5000")
                    print("6. 10000")
                    print("7. 20000")
                    print("8. Other")
                    user_choice = int(input())
                    if (user_choice == 1):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break
                    
                    elif (user_choice == 2):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 3):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 4):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 5):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break


                    elif (user_choice == 6):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 7):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 8):
                        other_amount = int(input("Enter an amount : "))
                        time.sleep(1)
                        print("Cash is Counted")
                        time.sleep(1)
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break
                if (user_choice == 2):
                    time.sleep(1)
                    print("Enter an amount")
                    print("1. 1000")
                    print("2. 2000")
                    print("3. 3000")
                    print("4. 4000")
                    print("5. 5000")
                    print("6. 10000")
                    print("7. 20000")
                    print("8. Other")
                    user_choice = int(input())

                    if (user_choice == 1):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 2):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 3):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 4):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 5):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break


                    elif (user_choice == 6):
                        print("Cash is Counted")
                        time.sleep(1)
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 7):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break


                    elif (user_choice == 8):
                        other_amount = int(input("Enter an amount : "))
                        time.sleep(1)
                        print("Cash is Counted")
                        time.sleep(1)
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break


            # If user choice is savings
            elif (user_choice == 2):
                time.sleep(1)
                print("Do you want a receipt for this transaction? ")
                print("1. Yes")
                print("2. No")
                user_choice = int(input())
                if (user_choice == 1):
                    print("Sorry, Receipts are not available at this time")
                    time.sleep(1)
                    print("Enter an amount")
                    print("1. 1000")
                    print("2. 2000")
                    print("3. 3000")
                    print("4. 4000")
                    print("5. 5000")
                    print("6. 10000")
                    print("7. 20000")
                    print("8. Other")
                    user_choice = int(input())
                    if (user_choice == 1):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break
                    
                    elif (user_choice == 2):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 3):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 4):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 5):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break


                    elif (user_choice == 6):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 7):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 8):
                        other_amount = int(input("Enter an amount : "))
                        time.sleep(1)
                        print("Cash is Counted")
                        time.sleep(1)
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break
                if (user_choice == 2):
                    time.sleep(1)
                    print("Enter an amount")
                    print("1. 1000")
                    print("2. 2000")
                    print("3. 3000")
                    print("4. 4000")
                    print("5. 5000")
                    print("6. 10000")
                    print("7. 20000")
                    print("8. Other")
                    user_choice = int(input())

                    if (user_choice == 1):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 2):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 3):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 4):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 5):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break


                    elif (user_choice == 6):
                        print("Cash is Counted")
                        time.sleep(1)
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 7):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break


                    elif (user_choice == 8):
                        other_amount = int(input("Enter an amount : "))
                        time.sleep(1)
                        print("Cash is Counted")
                        time.sleep(1)
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break
            
            # If user choice is joint
            elif (user_choice == 3):
                time.sleep(1)
                print("Do you want a receipt for this transaction? ")
                print("1. Yes")
                print("2. No")
                user_choice = int(input())
                if (user_choice == 1):
                    print("Sorry, Receipts are not available at this time")
                    time.sleep(1)
                    print("Enter an amount")
                    print("1. 1000")
                    print("2. 2000")
                    print("3. 3000")
                    print("4. 4000")
                    print("5. 5000")
                    print("6. 10000")
                    print("7. 20000")
                    print("8. Other")
                    user_choice = int(input())
                    if (user_choice == 1):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break
                    
                    elif (user_choice == 2):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 3):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 4):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 5):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break


                    elif (user_choice == 6):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 7):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 8):
                        other_amount = int(input("Enter an amount : "))
                        time.sleep(1)
                        print("Cash is Counted")
                        time.sleep(1)
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break
                if (user_choice == 2):
                    time.sleep(1)
                    print("Enter an amount")
                    print("1. 1000")
                    print("2. 2000")
                    print("3. 3000")
                    print("4. 4000")
                    print("5. 5000")
                    print("6. 10000")
                    print("7. 20000")
                    print("8. Other")
                    user_choice = int(input())

                    if (user_choice == 1):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 2):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 3):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 4):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 5):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break


                    elif (user_choice == 6):
                        print("Cash is Counted")
                        time.sleep(1)
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 7):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break


                    elif (user_choice == 8):
                        other_amount = int(input("Enter an amount : "))
                        time.sleep(1)
                        print("Cash is Counted")
                        time.sleep(1)
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break


            # If user choice is zero
            elif (user_choice == 4):
                time.sleep(1)
                print("Do you want a receipt for this transaction? ")
                print("1. Yes")
                print("2. No")
                user_choice = int(input())
                if (user_choice == 1):
                    print("Sorry, Receipts are not available at this time")
                    time.sleep(1)
                    print("Enter an amount")
                    print("1. 1000")
                    print("2. 2000")
                    print("3. 3000")
                    print("4. 4000")
                    print("5. 5000")
                    print("6. 10000")
                    print("7. 20000")
                    print("8. Other")
                    user_choice = int(input())
                    if (user_choice == 1):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break
                    
                    elif (user_choice == 2):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 3):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 4):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 5):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break


                    elif (user_choice == 6):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 7):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 8):
                        other_amount = int(input("Enter an amount : "))
                        time.sleep(1)
                        print("Cash is Counted")
                        time.sleep(1)
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break
                if (user_choice == 2):
                    time.sleep(1)
                    print("Enter an amount")
                    print("1. 1000")
                    print("2. 2000")
                    print("3. 3000")
                    print("4. 4000")
                    print("5. 5000")
                    print("6. 10000")
                    print("7. 20000")
                    print("8. Other")
                    user_choice = int(input())

                    if (user_choice == 1):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 2):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 3):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 4):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 5):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break


                    elif (user_choice == 6):
                        print("Cash is Counted")
                        time.sleep(1)
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

                    elif (user_choice == 7):
                        print("Cash is Counted")
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break


                    elif (user_choice == 8):
                        other_amount = int(input("Enter an amount : "))
                        time.sleep(1)
                        print("Cash is Counted")
                        time.sleep(1)
                        print("Cash Retract is disabled")
                        time.sleep(5)
                        print("Please take your cash")
                        time.sleep(3)
                        print("Do you want to perform another transaction? ")
                        print("1. Yes")
                        print("2. No")
                        user_choice = int(input())
                        if (user_choice == 1):
                            continue
                        else:
                            print("Thank you for using our service!")
                            break

