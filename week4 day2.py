'''import random
students = ["Chizaram", "Grace", "Praise", "Samson", "Abigail"]

for name in students:
    print ("Good morning", name)

visitor = input("What is your name? ")
if visitor in students:
    print(f"Welcome back {visitor}!")
else:
    print ("Sorry", visitor, "You're not in this class")

winner = random.choice(students)
print(f"Today's winner is: {winner}")




#team picker
import random
register = []
print("==CLASS REGISTER==")
for number in range(4):
    name = input("Enter a student name: ")
    register.append(name)
print("Register saved: ", register)

print("Calling the register. . .")
for name in register:
    print(f"{name}-present!")
print(f"Total students: {len(register)}")
check = input("Which student do you want to check for? ")
if check in register:
    print(f"Yes, {check} is in this class")
else:
    print(f"No {check} is not in this class")
star = random.choice(register)
print(f"THE STAR OF THE DAY IS {star}")
'''
#team picker2
import random

players = []

# Collect 6 player names
for player in range(6):
    name = input("Enter player name: ")
    players.append(name)

# Print all players
print("\nPlayers are:")
for name in players:
    print(name)

# Check if a person is playing
search_name = input("\nEnter a name to check if they are playing: ")

if search_name in players:
    print(search_name, "is playing!")
else:
    print(search_name, "is not playing.")

# Pick captains
red_captain = random.choice(players)
blue_captain = random.choice(players)

# Print captains
print("\nTEAM RED CAPTAIN:", red_captain + "!!!")
print("TEAM BLUE CAPTAIN:", blue_captain + "!!!")
