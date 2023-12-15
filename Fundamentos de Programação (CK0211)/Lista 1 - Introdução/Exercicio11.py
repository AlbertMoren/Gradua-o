# A program that calculates and displays the area of a rhombus. It is known that: A = (larger diagonal * smaller diagonal) / 2

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Input the values for the larger and smaller diagonals
diagonal_M, diagonal_m = input("Enter the values for the larger and smaller diagonals separated by a space: ").split(" ")

# Convert the inputs to float
diagonal_M = float(diagonal_M)
diagonal_m = float(diagonal_m)

# Calculate the area of the rhombus
area = (diagonal_M * diagonal_m) / 2

# Print the result
print(f"The area is = {area:.2f}")
