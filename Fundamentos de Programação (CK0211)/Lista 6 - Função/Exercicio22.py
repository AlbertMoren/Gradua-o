'''Create a program that:
■ use a subroutine to receive the elements of a 10X5 matrix of real numbers;
■ use a subroutine to calculate the sum of all elements located below the sixth line
of this matrix; 
The results should be shown in the main program.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def create_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [float(input(f"Enter element at position ({i + 1}, {j + 1}): ")) for j in range(cols)]
        matrix.append(row)
    return matrix

def calculate_sum_below_sixth_row(matrix):
    total_sum = 0
    for i in range(5):  # Columns
        for j in range(5, 10):  # Rows below the sixth row
            total_sum += matrix[j][i]
    return total_sum

# Create a 10x5 matrix using the create_matrix function
matrix = create_matrix(10, 5)

# Display the original matrix
print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Call the subroutine
sum_below_sixth_row = calculate_sum_below_sixth_row(matrix)

# Display the result
print(f"\nThe sum of elements below the sixth row is: {sum_below_sixth_row}")
