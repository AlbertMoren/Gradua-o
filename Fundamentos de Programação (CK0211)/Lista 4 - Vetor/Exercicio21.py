# Read a vector with ten positions for integers. Create a second vector, replacing null values with 1. Display both vectors.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

# Initialize the vectors
original_vector = []
modified_vector = []

# Receive values for the vector
print("Enter ten integer values:")
for i in range(10):
    value = int(input(f"Enter element {i+1}: "))
    original_vector.append(value)

# Create a second vector replacing null values with 1
for num in original_vector:
    if num == 0:
        modified_vector.append(1)
    else:
        modified_vector.append(num)

# Display the original and modified vectors
print("\nOriginal Vector:", original_vector)
print("Modified Vector:", modified_vector)
