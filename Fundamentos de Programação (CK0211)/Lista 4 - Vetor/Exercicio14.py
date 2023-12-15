# Receive names and two grades of six students and show the report as described:
# "Enter the name of the 1st student:", "Enter the 1st grade of Carlos:", ..., "Enter the 2nd grade of Carlos:".
# Display the report of names, grades, averages, and situations.
# Calculate and display the class average, percentage of approved students, percentage of students needing an exam,
# and percentage of failed students.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

names = []
grades1 = []
grades2 = []

for i in range(6):
    name = input(f"Enter the name of the {i+1}st student: ")
    grade1 = float(input(f"Enter the 1st grade of {name}: "))
    grade2 = float(input(f"Enter the 2nd grade of {name}: "))
    names.append(name)
    grades1.append(grade1)
    grades2.append(grade2)

print("\nReports of grades:")
print("STUDENT | 1st GRADE | 2nd GRADE | AVERAGE | STATUS")

total_students = len(names)
total_approved = 0
total_exam = 0
total_failed = 0

for i in range(total_students):
    average = (grades1[i] + grades2[i]) / 2
    status = "Approved" if average >= 5.0 else "Failed" if average < 4.0 else "Exam"
    print(f"{names[i]} | {grades1[i]:.1f} | {grades2[i]:.1f} | {average:.1f} | {status}")

    if status == "Approved":
        total_approved += 1
    elif status == "Exam":
        total_exam += 1
    else:
        total_failed += 1

class_average = sum((grades1[i] + grades2[i]) / 2 for i in range(total_students)) / total_students
percentage_approved = (total_approved / total_students) * 100
percentage_exam = (total_exam / total_students) * 100
percentage_failed = (total_failed / total_students) * 100

print("\nClass statistics:")
print(f"Class average = {class_average:.2f}")
print(f"Percentage of approved students = {percentage_approved:.2f}%")
print(f"Percentage of students needing an exam = {percentage_exam:.2f}%")
print(f"Percentage of failed students = {percentage_failed:.2f}%")
