word = "please"
attempts = 0
guess = input("What is the magic word? ")
while guess != word:
    guess = input("What is the magic word? ")
    attempts += 1
if guess == word:
    attempts = attempts + 1
    print(f"Good job, you got it in {attempts} attempts")
else:
    print(f"{guess} is not the magic word try again!")
    
    
    
