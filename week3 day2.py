'''# the for loop
name = input ("whats ur name")
for letter in name:
    print (letter)
'''
    #multiplication table
print("==TIMES TABLE MACHINE==")
table = int(input("which times table do you want"))
how_far = int(input("multiply up to what number? "))
for i in range(1, how_far+1):
        print(table,"*",i,"=", table * i)
