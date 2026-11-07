
print("Welcome To The Adventure Game.")


question1 = input("You See A Green And Red Door. Which One Do You Choose? ").lower().strip()

if question1 == "red":
    print("You Lose!, Game Over.")
elif question1 == "green":
    question2 = input("You See Two Alleys. Do You Want To Go Left Or Right? ").lower().strip()
    
    if question2 == "right":
        print("You Lose!")
    elif question2 == "left":
        question3 = input("You See A Dog Coming, Do You Run Or Do You Stay? ").lower().strip()
        
        if question3 == "stay":
            print("You Lose!")
        elif question3 == "run":
            question4 = input("You Get To A Cliff There Water Below Do You Jump Or Wait? ").lower().strip()
            if question4 == "wait":
                print("You Lose!")
            elif question4 == "jump":
                print("You Win!.")
            else:
                print("Invalid Choice, Game Over.")
        