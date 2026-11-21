activities = ["Morning Assembly", "Classroom Lessons", "Class-work/Exercises", "Break-Time", "Extra curricular-Activities"]

print(f"School Activities: {activities}\n")

print(f"First Activity: {activities[0]}")

print(f"Third Activity: {activities[2]}")

print(f"Last Activity: {activities[-1]}")

print(f"Total Number Of Activities: {len(activities)}\n")




for activity in activities:
    print(f"Today's Activity: {activity}")



index_num = int(input("Enter Index Number: "))

print(f"Activity: {activities[index_num]}")
