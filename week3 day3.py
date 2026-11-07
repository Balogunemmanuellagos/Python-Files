import random
'''
questions = [ ['what is 2 + 2?', '4'],
              ['capital of nigeria?', 'Abuja'],
              ['python is a ___ language', 'programming'],
              ['How many days are in a week?', '7'],
              ['What is the color of the sky?', 'blue']
    ]

random.shuffle(questions) # Mix the questions
score = 0

print('Welcome to the quiz app!! Answer 5 questions\n')

for i, q in enumerate(questions, 1):
    print(f'Q{i}: {q[0]}')
    answer = input("Enter your answer: ").strip().lower()

    if answer == q[1].lower():
        print('correct!\n')
        score += 1
    else:
        print(f'Wrong! correct answer {q[1]}\n')

print(f'Your final score: {score}/{len(questions)}')

if score == 5:
    print('Excellent!')
elif score >= 3:
    print('Good job!')
else:
    print('Keep practicing!')
'''

# for loop iterate(runs) over a list of items, e.g 1,2,3,4,5
# count to 10 but skip 5
'''for i in range(1, 11):
    if i == 5:
        continue # skip 5
    print(i)
   
for i in range(1, 11):
    if i == 5:
        continue # skip 5
    print(i)'''















'''
import random
#Number guessing game
secret= random.randint(1,20)
tries = 3

while tries >0:
    guess = int(input(f'Guess 1-20. Tries left{tries}: '))
    if guess == secret:
        print('You won! ')
        break # stops loop or ends when user wins
    elif guess < secret:
        print('Too low')
    else:
        print('Too High')
    tries -=1
else:
    print(f'Game over. The number was {secret}')













'''

#Iphone 45pro
correct_passcode = 'Adam123'
tries = 3
while tries >0:
    passcode = input('Enter passcode: ')
    if passcode =="":
        print('passcode cannot be empty')
        continue # skip don't reduce tries try
    
    if passcode == correct_passcode:
        print('Access granted')
        break #stops loop
    elif passcode == 'guest': #special case for later
        pass # placeholder - we'll add guess login later
    else:
        tries -= 1
        print('wrong passcode. Try again!')
else:
    print('Phone locked! please contact @support')


#Pass statement, 
names = ['Michael','Ada', 'Ngozi','Chizaram','Ama','Abigail' ]
for name in names:
    if name.strip() == 'Abigail':
        continue # skip item

    if name == 'Michael':
        print('Teacher Michael welcome in.Ending greetings.')
        continue # stops loop

    if name.startswith('Abigail'):
        pass # stop greeting everyone
    else:
        print(f'Hello, {name}! welcome!')
