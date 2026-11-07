score = int(input("Your score: "))

# Bonus rule
if score == 100 or score == 0:
    print("Special score!")

# Grade
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("Keep practising!")
