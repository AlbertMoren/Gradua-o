'''Create a program that receives the number of 10 students in a class, storing them in a vector, together
with the grades obtained throughout the semester (four assessments were carried out). Create subroutines to:
■ determine and display the arithmetic mean of all students;
■ indicate the number of students who must make recovery, that is, those with an average below 6.
Observation
All messages must be shown in the main program.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def calculate_average(grades):
    return sum(grades) / len(grades)

def students_needing_recovery(student_data):
    recovery_list = []
    for student, grades in student_data.items():
        average = calculate_average(grades)
        if average < 6:
            recovery_list.append(student)
    return recovery_list

# Receive input from the user
student_data = {}
for i in range(1, 11):
    student_number = int(input(f"Enter the number of student {i}: "))
    grades = [float(input(f"Enter grade {j} for student {i}: ")) for j in range(1, 5)]
    student_data[student_number] = grades

# Calculate and display the average for each student
print("\nAverage Grades for Each Student:")
for student, grades in student_data.items():
    average = calculate_average(grades)
    print(f"Student {student}: {average:.2f}")

# Identify students needing recovery
recovery_students = students_needing_recovery(student_data)

# Display the students needing recovery
if recovery_students:
    print("\nStudents Needing Recovery:")
    print(", ".join(map(str, recovery_students)))
else:
    print("\nAll students are above the passing grade.")
