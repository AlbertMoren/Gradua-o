# Receive fifteen numbers, determine and display:
# - the largest number and its position in the vector
# - the smallest number and its position in the vector.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")


# Initialize a vector
numbers_vector = []

# Receive values for the vector
print("Enter fifteen numbers:")
for i in range(15):
    value = float(input(f"Enter number {i+1}: "))
    numbers_vector.append(value)

# Determine the largest and smallest numbers along with their positions
max_number = max(numbers_vector)
min_number = min(numbers_vector)
max_position = numbers_vector.index(max_number)
min_position = numbers_vector.index(min_number)

# Display the results
print(f"\nThe largest number is {max_number} at position {max_position + 1}.")
print(f"The smallest number is {min_number} at position {min_position + 1}.")
