import random

# Elaborate a program that: receive the age of eight students and store them in a vector; store the code
# of five disciplines in another vector; store in a matrix the quantity of tests that each student took
# in each discipline.

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Elaborate a program that: receive the age of eight students and store them in a vector; store the code
# of five disciplines in another vector; store in a matrix the quantity of tests that each student took
# in each discipline.

def create_matrix(n_rows, n_columns, value):   # Create the desired matrix
    matrix = []  # empty list
    for i in range(n_rows):
        row = [] 
        for j in range(n_columns):
            row.append(value)		        
        matrix.append(row)	
    return matrix

# Initialize vectors and matrix
ages = []
discipline_codes = []
test_matrix = create_matrix(8, 5, 0)

# User input for age information
print("\nEnter the age of eight students:")
ages = [int(input(f"Enter age for student {i + 1}: ")) for i in range(8)]

# User input for discipline codes
print("\nEnter the code for five disciplines:")
discipline_codes = [input(f"Enter code for discipline {i + 1}: ") for i in range(5)]

# User input for test quantity matrix
print("\nEnter the quantity of tests for each student in each discipline:")
for i in range(8):
    for j in range(5):
        test_matrix[i][j] = int(input(f"Enter test quantity for student {i + 1} in discipline {discipline_codes[j]}: "))

# Display the entered information
print("\nEntered Information:")
print("Ages of Students:", ages)
print("Discipline Codes:", discipline_codes)
print("Test Matrix:")
for row in test_matrix:
    print(row)

# Calculate and display the required information
user_input_code = input("Enter a discipline code to check: ")

# Calculate the quantity of students with age between 18 and 25 who did more than two tests in the given discipline
try:
    discipline_index = discipline_codes.index(user_input_code)
    qualified_students = [i for i in range(8) if 18 <= ages[i] <= 25 and test_matrix[i][discipline_index] > 2]
    print(f"\nStudents aged between 18 and 25 who did more than two tests in {user_input_code}: {qualified_students}")
except ValueError:
    print("\nError: Discipline code not found.")

# List students who did less than three tests in any discipline along with the respective discipline code
print("\nStudents who did less than three tests in any discipline:")
for i in range(8):
    for j in range(5):
        if test_matrix[i][j] < 3:
            print(f"Student {i + 1} did {test_matrix[i][j]} tests in discipline {discipline_codes[j]}")

# Calculate and display the average age of students who did not take any test in any discipline
students_no_tests = [i for i in range(8) if all(test_matrix[i][j] == 0 for j in range(5))]
if students_no_tests:
    average_age = sum(ages[i] for i in students_no_tests) / len(students_no_tests)
    print(f"\nAverage age of students who did not take any test: {average_age:.2f}")
else:
    print("\nNo students found who did not take any test.")
