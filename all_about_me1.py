#the code below asks questions about the user in which the user type in his or her information; these informations are storedin their variables 
name = input("What is your name? ")
age = int(input("How old are you? "))
favourite_food = input("What is your favorite food? ")
favourite_colour = input("What is your favorite color? ")
dream_job = input("What is the name of your dream job? ")

# This code below is used to calculate the months gotten from the age
age_in_month = age * 12
# These code below, uses the print function to display the information of the user, which was stored in the various variables
print("===============================")
print(f"*   ALL ABOUT {name:<16}*")
print("===============================")
print(f"* Name:  {name:<21}*")
print(f"* Age: {age} (that is {age_in_month} months)*")
print(f"* Favourite food:  {favourite_food:<11}*")
print(f"* Favourite colour:  {favourite_colour:<9}*")
print(f"* Dream job:  {dream_job:<16}*")

print("===============================")
