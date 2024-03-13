# A program to mimic Glo's Ussd service. Assuming the user already dialed *312#

first_format = """
1 = Buy Data
2 = Gift Data
3 = Share Data
4 = Check Data Bal
5 = Voice / Data Roaming Offers
6 = Glo Reward - CashToken
0 = Exit
"""
print(first_format)
number = int(input("Enter a number : "))

if (number == 1):
    format = """
    1 = Proceed (Auto-renew)
    2 = Proceed (One-off)
    99 = Back
    0 = Exit
    """
    print(format)

    inside = int(input("Enter a number : ")) # Auto-Renew
    if (inside == 1):
        format1 = """
        1 = Mini Plans
        2 = Monthly Plans
        3 = Mega Plans
        4 = Super Mega Plans
        5 = Special Data Offer
        6 = Social Bundles
        7 = Night and Weekend Plans
        8 = GLOTV Plans 
        """
        print(format1)
        inside1 = int(input("Enter a number : "))
        if (inside1 == 1):
            format_1 = """
            1 = N100 = 150MB 1 Day incl 35MB nite
            2 = N200 = 350MB 2 Day incl 110MB nite
            3 = N500 = 1.8GB 14 Days incl 1GB nite
            4 = N50 = 50MB 1 Day incl 5MB nite
            """
            print(format_1)

            inside_2 = int(input("Enter a number : "))
            if (inside_2 == 1):
                print(f"Activation of 150MB 1 Day incl 35MB nite is successful and will expire tomorrow. See messages for full details")
            elif (inside_2 == 2):
                print(f"Activation of 350MB 2 Day incl 110MB nite is successful and will expire 15/03/2024 at 15:15pm. See messages for full details")
            elif (inside_2 == 3):
                print(f"Activation of 1.8GB 1 Day incl 1GB nite is successful and will expire on 14/04/2024. See messages for full details")
            elif (inside_2 == 4):
                print(f"Activation of 50MB 1 Day incl 5MB nite is successful and will expire on 14/04/2024 qt 15:15pm. See messages for full details")
        elif (inside1 == 2):
            format3 = """
            1 = N1000 = 3.9GB 30 Days incl 2GB nite
            2 = N1500 = 7.5GB 30 Day incl 4GB nite
            3 = N2000 = 9.2GB 30 Days incl 4GB nite
            4 = N2500 = 10.8GB 30 Day incl 4MB nite
            5 = More Plans
            99 = Back
            0 = Exit
            """
            print(format3)
            inside_2 = int(input("Enter a number : "))
            if (inside_2 == 1):
                print(f"Activation of One-Off 3.9GB 1 Day incl 35MB nite is successful and will expire 14/04/2024 at 15:15pm. See messages for full details")
            elif (inside_2 == 2):
                print(f"Activation of One-Off 7.5GB 2 Day incl 110MB nite is successful and will expire 15/03/2024 at 15:15pm. See messages for full details")
            elif (inside_2 == 3):
                print(f"Activation of One-Off 9.2GB 1 Day incl 1GB nite is successful and will expire on 14/04/2024. See messages for full details")
            elif (inside_2 == 4):
                print(f"Activation of One-Off 10.8GB 1 Day incl 5MB nite is successful and will expire on 14/04/2024 qt 15:15pm. See messages for full details")


    elif (inside == 2): # One-Off
        format2 = """
    1 = Mini Plans
    2 = Monthly Plans
    3 = Mega Plans
    4 = Super Mega Plans
    5 = Special Data Offer
    6 = Social Bundles
    7 = Night and Weekend Plans
    8 = GLOTV Plans 
    """
        print(format2)
        inside1 = int(input("Enter a number : "))
        if (inside1 == 1):
            format_1 = """
            1 = N100 = 150MB 1 Day incl 35MB nite
            2 = N200 = 350MB 2 Day incl 110MB nite
            3 = N500 = 1.8GB 14 Days incl 1GB nite
            4 = N50 = 50MB 1 Day incl 5MB nite
            """
            print(format_1)
            inside_2 = int(input("Enter a number : "))
            if (inside_2 == 1):
                print(f"Activation of One-Off 150MB 1 Day incl 35MB nite is successful and will expire 14/04/2024 at 15:15pm. See messages for full details")
            elif (inside_2 == 2):
                print(f"Activation of One-Off 350MB 2 Day incl 110MB nite is successful and will expire 15/03/2024 at 15:15pm. See messages for full details")
            elif (inside_2 == 3):
                print(f"Activation of One-Off 1.8GB 1 Day incl 1GB nite is successful and will expire on 14/04/2024. See messages for full details")
            elif (inside_2 == 4):
                print(f"Activation of One-Off 50MB 1 Day incl 5MB nite is successful and will expire on 14/04/2024 qt 15:15pm. See messages for full details")
                
        elif (inside == 2):
            format3 = """
            1 = N1000 = 3.9GB 30 Days incl 2GB nite
            2 = N1500 = 7.5GB 30 Day incl 4GB nite
            3 = N2000 = 9.2GB 30 Days incl 4GB nite
            4 = N2500 = 10.8GB 30 Day incl 4MB nite
            5 = More Plans
            99 = Back
            0 = Exit
            """
            print(format3)
            inside_2 = int(input("Enter a number : "))
            if (inside_2 == 1):
                print(f"Activation of One-Off 3.9GB 1 Day incl 35MB nite is successful and will expire 14/04/2024 at 15:15pm. See messages for full details")
            elif (inside_2 == 2):
                print(f"Activation of One-Off 7.5GB 2 Day incl 110MB nite is successful and will expire 15/03/2024 at 15:15pm. See messages for full details")
            elif (inside_2 == 3):
                print(f"Activation of One-Off 9.2GB 1 Day incl 1GB nite is successful and will expire on 14/04/2024. See messages for full details")
            elif (inside_2 == 4):
                print(f"Activation of One-Off 10.8GB 1 Day incl 5MB nite is successful and will expire on 14/04/2024 qt 15:15pm. See messages for full details")



    elif (inside == 99):
        format3 = """
        1 = Buy Data
        2 = Gift Data
        3 = Share Data
        4 = Check Data Bal
        5 = Voice / Data Bal
        6 = Glo Reward - CashToken
        0 = Exit
    """
        print(format3)
    elif (inside == 0):
        print("Glo, Rule your World")
    else:
        print("Not recognized, try again")

elif (number == 2):
    format1 = """
    1 = Mini Plans
    2 = Monthly Plans
    3 = Mega Plans
    4 = Super Mega Plans
    5 = Special Data Offer
    6 = Social Bundles
    7 = Night and Weekend Plans
    8 = GLOTV Plans 
    """
    print(format1)
    inside1 = int(input("Enter a number : "))
    if (inside1 == 1):
            format_1 = """
            1 = N100 = 150MB 1 Day incl 35MB nite
            2 = N200 = 350MB 2 Day incl 110MB nite
            3 = N500 = 1.8GB 14 Days incl 1GB nite
            4 = N50 = 50MB 1 Day incl 5MB nite
            """
            print(format_1)
            inside_2 = int(input("Enter a number : "))
            if (inside_2 == 1):
                usr_number = int(input("Enter a number to gift: "))
                print(f"Please press 0 to confirm if you want to gift {usr_number} N100 = 150MB 1 Day incl 35MB")
                container = int(input())
                print("Sorry, You are not viable to use this feature")

elif (number == 3):
    format1 = """
    1 = Share Data
    2 = Unshare Data
    3 = List of Shared Data
    4 = Get Data Settings
    5 = Manual Configuration Settings
    6 = Easy Share (Credit Share)
    0 = Exit 
    """
    print(format1)

elif (number == 4):
    print("Dear Customer, your plan has expired and you do not have a data plan. To buy a data plan and continue browsing, visit https://hsi.glo.com or dial *312#.")

elif (number == 5):
    format1 = """
    1 = My Tariff Plan
    2 = Int'l Call Offers
    3 = Data Roaming Offers
    4 = Berekete 10x
    5 = Glo 10Kobo
    6 = Always On
    99 = Back
    0 = Exit 
    """
    print(format1)

elif (number == 6):
    format1 = """
    Recharge and Win assured cashback, exciting prizes and a chance to win 100M every week
    1 = Opt-in
    2 = Opt-out
    99 = Back
    0 = Exit 
    """
    print(format1)

else:
    print("USSD must be 1-150 characters of length. Please try again")