#List: is a collection of items
mylist = [1,2,3,4,5,6,7,8,9,10, 1000]
print(mylist)
'''
x = 6
name = 'ALEX'
#Check what kind of data is my list
print(type(mylist))
print(type(x))
print(type(name))'''
'''
#Accessing Element In A List
print(mylist[0])
print(mylist[6])
print(mylist[::8])
print(mylist[::8])
print(mylist[2:10:3])# slicing of list

# Negative indexing
print(mylist[-1])
print(mylist[-2])
'''
# Random module
import random
'''
print(random.randint(1,6))

even_num = random.randrange(10, 51, 2 )
print("Random even number:", even_num)


#Random name picker
students = ['Ada', 'Bola', 'chinedu', 'Fatima', 'emeka']
chosen = random.choice(students)
print('Sweeper of the day', chosen)


# Random character
chars = "ABC123"
char = random.choice(chars)
print('Random characters ',char)


#Lottery
lottery = random.sample(range(1, 51),5)
print('Your lottery number',sorted(lottery))


#Shuffle function Deck of card
cards = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(cards)
print("shuffle deck" ,cards)
'''
# For loop

code = 'python'
for i in code:
    print(i)






    

# range function
for y in range(5):
    print('hello')


for j in range(10):
    print(j)




# coin flip 5 times
head = 0
tails = 0

for i in range(5):
    flip = random.choice(["Heads", "Tails"])
    print(flip)
    if flip == "Heads":
        head += 1
    else:
        tails += 1
print(f"Total: {head} Heads, {tails} Tails")
print(random.randint(1, 3))






















