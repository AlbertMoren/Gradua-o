# Read a vector with fifteen positions for integers. After reading, divide all its elements by the largest value in the vector. Show the vector after the calculations.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

# Initialize the input vector
input_vector = []

# Receive values for the input vector
print("Enter fifteen integer values for the vector:")
for i in range(15):
    value = int(input(f"Enter element {i+1}: "))
    input_vector.append(value)

# Find the maximum value in the vector
max_value = max(input_vector)

# Divide all elements in the vector by the maximum value
result_vector = [num / max_value for num in input_vector]

# Display the resulting vector
print("\nResulting vector after division by the maximum value:", result_vector)
