# Read a vector with fifteen positions for integers. Create a resulting vector that contains all prime numbers from the entered vector. Write the resulting vector.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

# Initialize the input vector
input_vector = []

# Receive values for the input vector
print("Enter fifteen integer values for the vector:")
for i in range(15):
    value = int(input(f"Enter element {i+1}: "))
    input_vector.append(value)

# Create the resulting vector with prime numbers
result_vector = []

# Check and add prime numbers to the resulting vector
for num in input_vector:
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            result_vector.append(num)

# Display the resulting vector
print("\nResulting vector with prime numbers:", result_vector)