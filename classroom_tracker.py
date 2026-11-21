equipment = ['projector', 'whiteboard', 'marker', 'computer']

print(f"Equipments: {equipment}")

add_piece = input("Enter New Piece Of Equipment: ")

equipment.append(add_piece)

remove_piece = input("Enter Equipment To Remove: ")

if remove_piece in equipment:
    equipment.remove(remove_piece)
    
else:
    print("Equipment not found.")


print("New Shopping Equipments:\n",equipment)

print(f"Total Number Of Equipment: {len(equipment)}")


for equipments in equipment:
    print(f"Available Items:\n{equipments}")




search_item = input("Enter equipment to search for: ")

if search_item in equipment:
    print("This equipment is available.")
else:
    print("This equipment is not available.")
