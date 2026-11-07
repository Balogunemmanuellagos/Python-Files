# Original
'''
radius = int(input("What Is The Radius? "))

area = 22/7 * radius ** 2

print(round(area, 2))
'''


# Enhanced

import time

name = input("* What Is Your Name? ")
try_again = True 

print("="*60)
print(f"* Welcome, {name} To The Circle Area Calculator. *")
print("="*60)


print("\n")

while try_again == True:

    radius = int(input("* Enter The Radius Of The Circle: "))

    area = 22/7 * radius ** 2

    print(f"* The Area Of The Circle Is: {area}")

    time.sleep(3)

    round_permission = input("* Do You Want To Round The Number? ").lower().strip()

    if round_permission == "yes" or round_permission == "y":
        time.sleep(2)
        round_num = int(input("* How Many Decimal Places Do You Want To Round To? "))
        time.sleep(2)
        print(f"* {area} Rounded To {round_num} Decimal Places Is {round(area, round_num)}.\n")
        
    elif round_permission == "no" or round_permission =="n":
        time.sleep(2)
        print(f"* The Area For The Circle Is {area}.\n")
        
    else:
        time.sleep(1)
        print(f"* {round_permission} Is Not Valid.\n")
        
    print("="*60)

    again = input("* Do You Want To Try Again? ").lower().strip()

    if again == "yes" or again == "y":
        try_again = True
    elif again == "no" or again == "n":
        print(f"* Thanks For Using The Circle Area Calculator; {name}.")
        try_again = False
    else:
        print(f"* {again} Is Not A Valid Answer.")
    print("="*60)