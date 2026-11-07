user_age = int(input("Input Your Age: ")) 

if user_age >= 7 and user_age <= 18:
    print("You Can Attend Python For Kids Class")
elif user_age >= 19 and user_age <= 40:
    print("You Can Attend Python For Youth Class")
else:
    print("You Can Attend Python For Adult Class")