'''

def lines():
    print("="*30)






def main():
    lines()
    try_again = True
    while try_again:
            no_1 = int(input("Input first number: "))
            no_2 = int(input("Input second number: "))
            sign = input("Enter sign: ")
            lines()
            if sign == "+":
                print(f"The sum of {no_1} and {no_2} is {no_1 + no_2}")
            elif sign == "-":
                print(f"The substraction of {no_1} and {no_2} is {no_1 - no_2}")
            elif sign == "*" or sign == "×":
                print(f"The multiplication of {no_1} and {no_2} is {no_1 * no_2}")
            elif sign == "/" or sign == "➗":
                print(f"The division of {no_1} and {no_2} is {no_1 / no_2}")
            else:
                print(f"{sign} is not a valid sign")
            lines()
            again = input("Do you want to try again? [YES OR NO]: ")
            if again.lower() == "yes":
                try_again = True
            elif again.lower() == "no":
                try_again = False
                print("Thank you for using the calculator.")
            else:
                print(f"{again} is not a valid answer")
                try_again = False
                try_again = False
            
            lines()




main()






number = 0


for number in range(1,11):
    print(number)
'''


for i in range(1, 6):
    print(i)

