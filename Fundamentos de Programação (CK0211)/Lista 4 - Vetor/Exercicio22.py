# Read a vector A of ten positions. Then, compact the vector, removing null and negative values. Store this result in vector B. Display vector B.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

# Initialize the vectors
vector_A = []
vector_B = []

# Receive values for vector A
print("Enter ten integer values:")
for i in range(10):
    value = int(input(f"Enter element {i+1}: "))
    vector_A.append(value)

# Compact the vector, removing null and negative values
for num in vector_A:
    if num > 0:
        vector_B.append(num)

# Display the compacted vector B
print("\nCompacted Vector B:", vector_B)
