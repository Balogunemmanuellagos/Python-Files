
print("=" * 60)
print("* Welcome to the Basic Calculator!🧮 *")
print("=" * 60)

first_number = int(input("* Enter your first number: "))
second_number = int(input("* Enter your second number: "))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = round(first_number / second_number, 2)

print(f"* Addition: {first_number} + {second_number} = {addition}")
print(f"* Subtraction: {first_number} - {second_number} = {subtraction}")
print(f"* Multiplication: {first_number} * {second_number} = {multiplication}")
print(f"* Division: {first_number} / {second_number} = {division}")