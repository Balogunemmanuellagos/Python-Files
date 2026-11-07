'''
# elif
# elif is used to check other options in python
colour = input("Type a traffic light colour: ")
if colour == "green":
    print("Go!")
elif colour == "Yellow":
    print("Slow down")
elif colour == "red":
    print("Stop")
else:
    print("error")


# and / or

#"and" both conditions must be true
age = 9
has_permission = True
if age >= 8  and has_permission == True:
    print("Welcome to the football club")
else:
    print("sorry you can't join yet")






# "or" needs at least one of the condition tobe true
day = "saturday"
if day == "Saturday" or day == "sunday":
    print("It is the weekend! no school")
else:
    print("School day, pack your bag")

'''




print("Welcome, young coder, to the sorting Ceremony")
name = input("What is your name? ")
print(f"Hmm... let me think about you, {name} . . .")
answer1 = input("Pick one: sword, book, ball, or pillow? ")
answer2 = input("pick one:  mountain, library, beach or garden?")
if answer1 == "sword" and answer2 == "mountain":
    print(f"{name}, a true adventurer . . . TEAM LION, aquad captain")
elif answer1 == "sword":
    print(f"{name}, you are brave . . . TEAM LION!")
elif answer1 == "book" or answer2 == "library":
    print(f"{name}, you are clever . . . TEAM EAGLE!")
elif answer1 == "ball" or answer2 == "beach":
    print(f"{name}, you are friendly . . . TEAM DOLPHIN!")
else:
    print(f"{name}, you are calm and steady . . . TEAM TORTOISE!")

    
