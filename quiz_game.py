#QUIZ PROGRAM

try_again = True;

while try_again:
    name = input("What is your name? ").lower()
    score = 0
    percentage = 0
    print(f"Hi {name}.")
    print("Below are mathematical questions, in which all are to be answered")
    # The while loop below is used to loop the questions again if try_again = true

    answer = int(input("Q1: What is the co-efficient of x in 2x? "))
    if answer == 2:


        print("Correct!")
        score = score + 1
        percentage = percentage + 16.66
        
    else:
        print("Wrong!. The answer is 2.")
        

    answer = int(input("Q2: how many degrees does angle on a straight line sum up to (type just the number without the degree sign)? "))
    if answer == 180:
        print("Correct!")
        score = score + 1
        percentage = percentage + 16.66
        
    else:
        print("Not quite. The answer is 180.")
        

    answer = int(input("Q3: what is the square root of 196? "))
    if answer == 14:
        print("Correct!")
        score = score + 1
        percentage = percentage + 16.66
        
    else:
        print("Not quite. The answer is 14.")


    answer = int(input("Q4: If you have 24 cookies and share them equally among 4 friends, how many cookies does each friend get? "))
    if answer == 6:
        print("Correct!")
        score = score + 1
        percentage = percentage + 16.66
            
    else:
        print("Not quite. The answer is 6.")

    answer = input("Q5: Which shape has exactly 3 sides and 3 angles? ")
    if answer.lower() == "triangle":
        print("Correct!")
        score = score + 1
        percentage = percentage + 16.66
                
    else:
        print("Not quite. The answer is Triangle.")

    answer = int(input("Q5: What is the sum of 25 and 17? "))




    
    if answer == 42:
        print("Correct!")
        score = score + 1
        percentage = percentage + 16.66
                    
    else:
        print("Not quite. The answer is Triangle.")
# The if/elif/else below are used to condition the scores
    if score == 6 or score == 5:
        print(f"Excellent! {name}, you are a genius. You scored {score}/6. Your percentage is {round(percentage, 1)}%")
    elif score == 4 or score == 3:
        print(f"Bravo! {name}, you did a great job. You scored {score}/6. Your percentage is {round(percentage, 1)}%")
    else:
        print(f"Try again {name} and also keep practicing. You scored {score}/6. Your percentage is {round(percentage, 1)}%")

# the try_again varieble, with the input function is used to ask the user if he or she wants to try again    
    again = input("Do you want to try again(YES/NO)? ")
    # the if condition below, is used to check if again == yes.
    if again.lower() == "yes":
        try_again = True
        
    else:
        try_again = False
        print("\nWeldone! and Thanks for playing!")
