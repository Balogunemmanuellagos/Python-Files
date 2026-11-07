 # Balogun Emmanuel. A number guessing game where you have 5 tries to find a secret number.


# below is the code used to import random

import random

# The Play_game() function contains all the main code for the number guessing game

def play_game():
    
    name = input("* Enter Your Name: ")

    secret_number = random.randint(1, 20)

    tries_left = 5

    print("=" *  100)

    print(f"* Welcome, {name}! Guess the secret number between 1 and 20. You have 5 tries. Good luck! *")

    print("=" *  100)

    

# The while loop below is used to loop the question guess the number (1-20) ,if guess is not equals to secret 

    

    while tries_left > 0:

            player_guess = int(input("\n* Guess the secret number (1-20): "))

# The if statement below is used to check if the player guess is equal to the secret number, if it is then the player wins and the loop breaks, if not then the player is told if their guess is too low or too high and the number of tries left is decremented by 1
    
            if player_guess == secret_number:

                print("* Correct! You win.\n")

                break

            if player_guess < secret_number:

                print("* Too low!")

            else:

                print("* Too high!")


            tries_left -= 1

            print(f"* You have {tries_left} tries left. Keep going!")


# The if statement below is used to check if the player has run out of tries, if they have then the player is told they are out of tries and the secret number is revealed

            if tries_left == 0:

                print(f"\n* {name}, you are out of tries! The number was {secret_number}.")

                print("* Better luck next time!")
                
                print("=" *  100)

                break


# The code below ask the player if they want to play again, if they do then the play_game() function is called, if not then the game ends


    again = input("\n* Do you want to try again? ").strip().lower()

    if again == "yes":

        play_game()

    elif again == "no":

        print("* Thank you for playing!\n")

        print("=" *  100)

        

    else:

        print(f"* {again} IS An Invalid input.")

        print("* Thank you for playing!\n")

            




# The code below is used to call the play_game() function

play_game()































'''
 # Balogun Emmanuel. A number guessing game where you have 5 tries to find a secret number.


# below is the code used to import random

import random


# The Play_game() function contains all the main code for the number guessing game

def play_game():
    
    name = input("* Enter Your Name: ")
    secret_number = random.randint(1, 20)
    tries_left = 5

    print("=" *  100)
    print(f"* Welcome, {name}! Guess the secret number between 1 and 20. You have 5 tries. Good luck!")
    print("=" *  100)

	# The while loop below is used to loop the question guess the number (1-20) ,if guess is not equals to secret 

    while tries_left > 0:
        player_guess = int(input("\n* Guess the secret number (1-20): "))

	# The if statement below is used to check if the player guess is equal to the secret number, if it is then the player wins and the loop breaks, if not then the player is told if their guess is too low or too high and the number of tries left is decremented by 1
 
        if player_guess == secret_number:
            print("* Correct! You win.\n")
            break

        if player_guess < secret_number:
            print("* Too low!")
        else:
            print("* Too high!")

        tries_left -= 1
        print(f"* You have {tries_left} tries left. Keep going!")

		# The if statement below is used to check if the player has run out of tries, if they have then the player is told they are out of tries and the secret number is revealed

        if tries_left == 0:
            print(f"\n* {name}, you are out of tries! The number was {secret_number}.")
            print("* Better luck next time!")
            
# The code below is used to call the play_game() function and ask the player if they want to play again, if they do then the play_game() function is called again, if not then the game ends

play_game()

print("=" *  100)

again = input("\n* Do you want to try again? ").strip().lower()
if again == "yes":
    play_game()
else:
    print("* Thank you for playing!")
    print("=" *  100)


'''