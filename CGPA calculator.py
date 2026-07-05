print("===== PERSONAL POCKET CGPA CALCULATOR =====")

total_grade_points = 0
total_units = 0

while True:

    print("Grade")
    print("A = 5")
    print("B = 4")
    print("C = 3")
    print("D = 2")
    print("E = 1")
    print("F = 0")

    grade = input("Enter Grade (A-F): ").upper()

    if grade == "A":
        point = 5
    elif grade == "B":
        point = 4
    elif grade == "C":
        point = 3
    elif grade == "D":
        point = 2
    elif grade == "E":
        point = 1
    elif grade == "F":
        point = 0
    else:
        print("Invalid Grade")
        continue

    unit = int(input("Enter Course Unit: "))

    total_grade_points += point * unit
    total_units += unit

    option = input("Add another course? (Y/N): ")

    if option == "N":
        break

cgpa = total_grade_points / total_units

print("===== RESULT =====")
print("Total Units =", total_units)
print("Total Grade Points =", total_grade_points)
print("CGPA =", round(cgpa, 2))

if cgpa >= 4.50:
    print("Class: First Class")
elif cgpa >= 3.50:
    print("Class: Second Class Upper")
elif cgpa >= 2.40:
    print("Class: Second Class Lower")
elif cgpa >= 1.50:
    print("Class: Third Class")
else:
    print("Class: Pass")