
import random, time






def line():
    print("="*30)




def Player1():
    rand_values1 = random.choice([ "cake", "ice-cream", "van", "imposter"])
    rand_values2 = random.choice([ "cake", "ice-cream", "van", "imposter"])
    
   
    random.choice(rand_values1)    
    ai = random.choice
    
    question = int(input("How many players are playing this game (1-4 players)? "))

    if question == 1:
        line()
        name = input("INPUT YOUR NAME: ")
        load = [
            "Sending Message To AI...",
            "Sending Message To AI...",
            "Sending...",
            "Sent✓✓\n1"
        ]
        load2 = [
            "AI Typing Message...",
            "Message Sent By AI...",
            "Receiving Message...",
            "Received!!!"

        ]
        player1 = rand_values1
        ai_response = random.choice([ "I AM NOT THE IMPOSTER!!", f"{name.upper()} IS THE IMPOSTER!!"])
        line()
        print(f"{name.upper()} VERSUS AI")
        line()
        letter = input(f'{name.upper()}, Enter the letter "R" To reveal your word: ')

        if letter.lower() == "r":
            if player1 ==  "cake" or "ice-cream" or "van":

                print(f"{player1}, your word is {rand_values1}.")
                print("IT IS TIME TO DECIDE WHO THE IMPOSTER IS.")
                option = print("1. AI IS THE IMPOSTER.\n2. I AM NOT THE IMPOSTER")
                
                ans = int(input("Choose One: "))
                if ans == 1 or ans == 2:
                    for loads in load:
                        time.sleep(1)
                        print(loads)
                    
                    for loads2 in load2:
                        time.sleep(1)
                        print(loads2)
                    print(f"\nAI Said '{ai_response}'")            
                        
                    
                    print("First To Finish Typing Gets To Decide Who The Imposter Is Wins. Start typing in:")
                    time.sleep(5)
                    
                    print(f"AI Finishes In: ")
                    t = [5.,4.,3.,2.,1., "AI Is Done!!"]
                    for ts in t:
                        time.sleep(2)
                        print(ts)
                    print(ai_response)
                    
                    time.sleep(1)
                    
                    
                    

            if player1 == "imposter!":
                print(f"{player1}, you are the Imposter!")
                print("IT IS TIME TO DECIDE WHO THE IMPOSTER IS.")
                option = print("1. AI IS THE IMPOSTER.\n2. I AM NOT THE IMPOSTER")
                ans = input("Choose One: ")
                for loads in load:
                    time.sleep(1)
                    print(loads)

                for loads2 in loads2:
                    time.sleep(1)
                    print(loads2)
                
                ans = input("Choose One: ")
                if ans == 1 or ans == 2:
                    print("First To Finish Typing Gets To Decide Who The Imposter Is Wins. Start typing in:")
                    t = [3.,2.,1., "GO!!"]
                    for ts in t:
                       time.sleep(2)
                       print(ts)
                    final = input ("Type Here (I am not the imposter or I am the imposter): ")
            




              

Player1()















'''import random
def line():
    print("="*30)

ra
def Players():
    player1 = None
    player2 = None
    player3 = None
    player4 = None
    imp = "Imposter"
    rand_values = [ "", "", "", "", "", ""]
    question = int(input("How many players are playing this game (1-4 players)? "))

    if question == 1:
        line()
        name = input("INPUT YOUR NAME: ")
        line()
        print(f"{name} versus ai")
        line()
Players()'''
