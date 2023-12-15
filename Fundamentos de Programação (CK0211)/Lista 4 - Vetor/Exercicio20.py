# Read a vector with ten positions for integers and display only the positive numbers.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

# Initialize the vector
integer_vector = []

# Receive values for the vector
print("Enter ten integer values:")
for i in range(10):
    value = int(input(f"Enter element {i+1}: "))
    integer_vector.append(value)

# Display only the positive numbers
print("\nPositive numbers:")
for num in integer_vector:
    if num > 0:
        print(num)
