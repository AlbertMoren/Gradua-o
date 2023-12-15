# Receive names and grades of eight students and show the report as described:
# "Enter the name of the 1st student:", "Enter the grade of Carlos:", ..., "Enter the grade of Pedro:".
# Display the report of names and grades and calculate and display the class average.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

names = []
grades = []

for i in range(8):
    name = input(f"Enter the name of the {i+1}st student: ")
    grade = float(input(f"Enter the grade of {name}: "))
    names.append(name)
    grades.append(grade)

print("Reports of grades:")
for i in range(8):
    print(f"{names[i]} {grades[i]}")

class_average = sum(grades) / len(grades)
print(f"\nClass average = {class_average:.2f}")
