'''shopping_list = []
print ("Welcome to the Shopping List Helper!")
print ("Your list is empty right now.")

item1 = input ("Add your first item: ")
shopping_list.append (item1)

item2 = input ("Add your second item: ")
shopping_list.append (item2)

item3 = input ("Add your third item: ")
shopping_list.append (item3)

item4 = input ("Add your fourth item: ")
shopping_list.append (item4)

item5 = input ("Add your fifth item: ")
shopping_list.append (item5)

print (f"Your list:  {shopping_list}")
print (f"You have {len (shopping_list)} items on your list")
print("The second thing to buy is: ", shopping_list [len(shopping_list) -4] )
print("Please remove two items")
gone = input("Enter first item to remove: ")
gone2 = input("Enter second item to remove: ")
shopping_list. remove (gone)
shopping_list. remove (gone2)
print ("Removed", gone, "and", gone2,"!")
print ("Final list: ", shopping_list)
print ("Final count: ", len (shopping_list),"."," Goodbye!" )
'''





























import time

shopping_list = []
position_of_items = ["First", "Second", "Third", "Fourth"]
removing_load = [
    "Removing Item...",
    "Removing Item...",
    "Removing Item...",
    "Removing Item...",
    "Items Removed!!"
]

print ("Welcome to the Shopping List Helper!")
print ("Your list is empty right now.")

item1 = input ("Add your first item: ")
shopping_list.append (item1)

item2 = input ("Add your second item: ")
shopping_list.append (item2)

item3 = input ("Add your third item: ")
shopping_list.append (item3)

item4 = input ("Add your fourth item: ")
shopping_list.append (item4)

item5 = input ("Add your fifth item: ")
shopping_list.append (item5)

print("Your list:  ")
for shopping_lists in enumerate(shopping_list): 
    print (f"{shopping_lists}")


print (f"You have {len (shopping_list)} items on your list")

while True: 
    remove = input("Do You Want To Remove Any Item? ").lower().strip()

    if remove == "y" or remove == "yes": 
    
        no_of_item_to_remove = int(input("How Many Items Do You Want To Remove?(You Can Only Remove 4 Items):  "))
        if no_of_item_to_remove == 1: 
            gone1 = input("Enter Item To Remove: ")
            if gone1 in shopping_list: 
                for load in removing_load: 
                                time.sleep(1)
                                print(load)
                shopping_list.remove(gone1)
                print(f"{gone1} Is Removed From The List")
                print(f"New shopping_list:  {shopping_list}. You Have {len(shopping_list)} in Your List.")
            else:
                  print(f"{gone1} Is Not In The List You Created.")
        elif no_of_item_to_remove == 2: 
            gone1 = input(f"Enter {position_of_items[0]} item to remove: ").lower().strip()
            gone2 = input(f"Enter {position_of_items[1]} item to remove: ").lower().strip()
            if gone1 and gone2 in shopping_list:
                for load in removing_load:
                    time.sleep(1) 
                    print(load)

                shopping_list.remove(gone1)
                shopping_list.remove(gone2)
                print(f"{gone1} and {gone2} Are Removed From The List")
                print(f"New shopping_list:  {shopping_list}. You Have {len(shopping_list)} in Your List.")
            else:
                print(f"{gone1} Or {gone2} Are Not In The List You Created.")
        elif no_of_item_to_remove == 3: 
            gone1 = input(f"Enter {position_of_items[0]} item to remove: ").lower().strip()
            gone2 = input(f"Enter {position_of_items[1]} item to remove: ").lower().strip()
            gone3 = input(f"Enter {position_of_items[2]} item to remove: ").lower().strip()
            if gone1 and gone2 and gone3 in shopping_list:
                for load in removing_load:
                                time.sleep(1) 
                                print(load)

                shopping_list.remove(gone1)
                shopping_list.remove(gone2)
                shopping_list.remove(gone3)
                print(f"{gone1}, {gone2}, and {gone3} Are Removed From The List")
                print(f"New shopping_list:  {shopping_list}. You Have {len(shopping_list)} in Your List.")
            else:
                              print(f"{gone1}, {gone2} Or {gone3} Are Not In The List You Created.")
        elif no_of_item_to_remove == 4: 
            gone1 = input(f"Enter {position_of_items[0]} item to remove: ")
            gone2 = input(f"Enter {position_of_items[1]} item to remove: ")
            gone3 = input(f"Enter {position_of_items[2]} item to remove: ")
            gone4 = input(f"Enter {position_of_items[3]} item to remove: ")
            if gone1 and gone2 and gone3 and gone4 in shopping_list:
                for load in removing_load: 
                                time.sleep(1)
                                print(load)
                shopping_list.remove(gone1)
                shopping_list.remove(gone2)
                shopping_list.remove(gone3)
                shopping_list.remove(gone4)
                print(f"{gone1}, {gone2}, {gone3}, and {gone4} Are Removed From The List")
                print(f"New shopping_list:  {shopping_list}. You Have {len(shopping_list)} in Your List.")
            else:
               print(f"{gone1}, {gone2} Or {gone3} Are Not In The List You Created.")
        else: 
            print(f"{no_of_item_to_remove} Is Out Of Bound")
            True
    elif remove == "n" or remove == "no": 
        print(f"Final shopping_list:  {shopping_list}. You Have {len(shopping_list)} in Your List.")
        break
    else: 
        print(f"{remove} Is Not Valid. Please Enter Yes or No.")
        True
            









