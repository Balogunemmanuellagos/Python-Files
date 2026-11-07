# The code below is used to import fandom so I can use and access some random components and function
import random
# below are some variebles which would be decleared and re-asigned in the while loop
secret = random.randint(1, 50)
attempts = 0
guess = 0

# The while loop below is used to loop the question guess the number (1-50) ,if guess is not equals to secret 
while guess != secret:
    guess = int(input("Guess my number (1-50): "))
    attempts = attempts +1
    if guess > 50:
        print("You are to guess from number 1-50 ")
        attempts
    elif guess > secret:
        print('Lower! Try again.')
        attempts
    elif guess < secret: 
       print('Higher! Try again')
       attempts
       
    elif guess == secret:
        print(f"You got it in {attempts} tries! You are a mind reader!")
    
    else:
        print("You are to guess from number 1-50 ")
            
        
    
