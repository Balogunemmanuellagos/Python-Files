# Original
'''
base = int(input("What Is The Base? "))
height = int(input("What Is The Height? "))

area = 1/2 * base * height
print(round(area, 2))
'''


# Enhanced

import time

name = input("* What Is Your Name? ")
try_again = True 

print("="*60)
print(f"* Welcome, {name} To The Triangle Area Calculator. *")
print("="*60)


print("\n")

while try_again == True:

        height = int(input("* Enter The Height Of The Triangle: "))

        base = int(input("* Enter The Base Of The Triangle"))

        area = 1/2 * base * height

        print(f"* The Area Of The Triangle Is: {area}")

        time.sleep(3)

    

        round_permission = input("* Do You Want To Round The Number? ").lower().strip()

        if round_permission == "yes" or round_permission == "y":
            time.sleep(2)
            round_num = int(input("* How Many Decimal Places Do You Want To Round To? "))
            time.sleep(2)
            print(f"* {area} Rounded To {round_num} Decimal Places Is {round(area, round_num)}.\n")
            
        elif round_permission == "no" or round_permission =="n":
            time.sleep(2)
            print(f"* The Area For The Triangle Is {area}.\n")
            
        else:
            time.sleep(1)
            print(f"* {round_permission} Is Not Valid.\n")
            
        print("="*60)
    
        again = input("* Do You Want To Try Again? ").lower().strip()

        if again == "yes" or again == "y":
            try_again = True
        elif again == "no" or again == "n":
            print(f"* Thanks For Using The Triangle Area Calculator; {name}.")
            try_again = False
        else:
            print(f"* {again} Is Not A Valid Answer.")
        print("="*60)






     