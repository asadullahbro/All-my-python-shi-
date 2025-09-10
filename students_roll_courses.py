courses = ("Math", "English", "Science")
students = []
roll_number = set()

while True:
    name = input("Enter Student Name: (q to quit) ")
    if name == "q":
        break
    roll = input("Enter the roll number: ")
    if roll in roll_number:
        print("Roll Number Exists.")

    else:
        students.append((name, roll))
        roll_number.add(roll)
        print(f"Registered {name} with Roll: {roll}")

print("All Students:", students)

