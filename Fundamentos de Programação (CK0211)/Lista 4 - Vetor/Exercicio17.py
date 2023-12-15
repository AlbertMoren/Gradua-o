# Receive two vectors of ten positions each, determine and display a third vector containing the elements
# of the two previous vectors sorted in descending order.


# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

# Initialize two vectors
vector1 = []
vector2 = []

# Receive values for the first vector
print("Enter values for the first vector:")
for i in range(10):
    value = int(input(f"Enter the {i+1}th value: "))
    vector1.append(value)

# Receive values for the second vector
print("\nEnter values for the second vector:")
for i in range(10):
    value = int(input(f"Enter the {i+1}th value: "))
    vector2.append(value)

# Merge the two vectors
merged_vector = vector1 + vector2

# Sort in descending order
sorted_vector = sorted(merged_vector, reverse=True)

# Display the result
print("\nMerged and sorted vector in descending order:")
print(sorted_vector)
