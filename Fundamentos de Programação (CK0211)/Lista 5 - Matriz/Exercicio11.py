# Elaborate a program that: receive the age of eight students and store them in a vector; store the code
# of five disciplines in another vector; store in a matrix the quantity of tests that each student took
# in each discipline.

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def create_matrix(n_rows, n_columns, value):   # Create the desired matrix
    matrix = []  # empty list
    for i in range(n_rows):
        row = [] 
        for j in range(n_columns):
            row.append(value)		        
        matrix.append(row)	
    return matrix

# Initializing vectors and matrix
ages = []
discipline_codes = []
test_matrix = create_matrix(8, 5, 0)

# Input age information
for i in range(8):
    age = int(input(f"Enter the age of student {i + 1}: "))
    ages.append(age)

# Input discipline codes
for i in range(5):
    code = input(f"Enter the code for discipline {i + 1}: ")
    discipline_codes.append(code)

# Input test quantity for each student and discipline
for i in range(8):
    for j in range(5):
        test_quantity = int(input(f"Enter the quantity of tests student {i + 1} took in discipline {discipline_codes[j]}: "))
        test_matrix[i][j] = test_quantity

# Display the collected information
print("\nCollected Information:")
print("Ages of Students:", ages)
print("Discipline Codes:", discipline_codes)
print("Test Matrix:")
for row in test_matrix:
    print(row)
