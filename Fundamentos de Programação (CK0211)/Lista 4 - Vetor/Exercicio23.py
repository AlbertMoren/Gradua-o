# Read two vectors (A and B) with five positions for integer numbers. The program should then subtract the first element of A from the last of B, accumulating the value, subtract the second element of A from the second to last of B, accumulating the value and so on. Finally, display the result of all subtractions.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

# Initialize vectors A and B
vector_A = []
vector_B = []

# Receive values for vector A
print("Enter five integer values for vector A:")
for i in range(5):
    value = int(input(f"Enter element {i+1}: "))
    vector_A.append(value)

# Receive values for vector B
print("\nEnter five integer values for vector B:")
for i in range(5):
    value = int(input(f"Enter element {i+1}: "))
    vector_B.append(value)

# Subtract corresponding elements and accumulate the result
result = 0
for i in range(5):
    result += vector_A[i] - vector_B[4 - i]

# Display the result of all subtractions
print("\nResult of all subtractions:", result)
