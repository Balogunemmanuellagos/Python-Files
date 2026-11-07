# Balogun Emmanuel, Portfolio Programme 1, 2nd November 2026.




print("=" * 60)

# Welcome Message Below.

print('\t*Welcome To The "ALL ABOUT ME" Card Maker*')

print("=" * 60)

# Prompts used to ask user questions and giving the the opportunity to type their answers through the input function. 

name = input("\n* What Is Your Name? ")

age = int(input("* How Old Are You? "))

next_age = age + 1

favourite_food = input("* What Is Your Favourite Food? ")

dream_job = input("* What Is Your Dream Work? ")

favourite_colour = input("* What Is Your Favourite Colour? ")

favourite_game = input("* Kindly State Your Favourite Game: ")

favourite_subject = input("* What Is The Name Of Your Favourite Subject? ")

# The "\n" escape character is used to to make a new line.

print("\n")

print("=" * 60)

# Below Are The Output Of The Information Typed In with some ASCII border design.

print("* ALL ABOUT ME GREETING CARD *")

print("=" *  60)


print("┌───────────────────────────────────────────────────────────────┐")

print(f"| My Name Is: {name}.")

print(f"| I Am: {age} Years Old. Next year I Will Be {next_age} Years Old.")

print(f"| My Favourite Food Is: {favourite_food}.")

print(f"| I would Love To Become A/AN: {dream_job} In Future!.")

print(f"| My Favourite Colour Is: Colour {favourite_colour}.")

print(f"| My Favourite Game Is: {favourite_game}.")

print(f"| My Favourite Subject Is: {favourite_subject}.")

print("└───────────────────────────────────────────────────────────────┘")

print("=" *  60)


# below is the appreciation message to the user for using/visiting the program.

print(f"* Thanks For Visiting {name}! *")