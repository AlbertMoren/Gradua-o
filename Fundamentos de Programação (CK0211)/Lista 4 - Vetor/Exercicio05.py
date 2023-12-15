# Program Description:
# A school wants to know if there are students simultaneously taking Logic and Programming Language courses.
# Place the enrollment numbers of students taking Logic in one vector (15 students).
# Place the enrollment numbers of students taking Programming Language in another vector (10 students).
# Show the enrollment numbers that appear in both vectors.

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Initialize vectors
logic_students = set()
language_students = set()

# Input for Logic students
for i in range(15):
    matricula = int(input(f"Enter the enrollment number of the student {i + 1} taking Logic: "))
    logic_students.add(matricula)

# Input for Language students
for i in range(10):
    matricula = int(input(f"Enter the enrollment number of the student {i + 1} taking Programming Language: "))
    language_students.add(matricula)

# Find the intersection
common_students = logic_students.intersection(language_students)

# Display the common enrollment numbers
print("Enrollment numbers that appear in both Logic and Programming Language courses:", common_students)
