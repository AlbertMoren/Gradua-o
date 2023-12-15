# Read two vectors of ten positions and multiply corresponding elements, storing the result in a third vector. Display the resulting vector.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

# Initialize vectors
vector1 = []
vector2 = []
result_vector = []

# Receive values for the first vector
print("Enter values for the first vector:")
for i in range(10):
    value = float(input(f"Enter element {i+1}: "))
    vector1.append(value)

# Receive values for the second vector
print("\nEnter values for the second vector:")
for i in range(10):
    value = float(input(f"Enter element {i+1}: "))
    vector2.append(value)

# Multiply corresponding elements and store the result in the third vector
for i in range(10):
    result_vector.append(vector1[i] * vector2[i])

# Display the resulting vector
print("\nThe resulting vector after multiplication:")
print(result_vector)
