'''Create a subroutine that takes a vector X of 15 integers as a parameter and returns the
number of even values in X.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def count_even_values(vector):
    count = 0
    for value in vector:
        if value % 2 == 0:
            count += 1
    return count

# Function to get user input for the vector
def input_vector(size):
    vector = []
    for i in range(size):
        element = int(input(f"Enter element {i + 1}: "))
        vector.append(element)
    return vector

# User inputs the data
n = 15
X = input_vector(n)

# Calling the subroutine
even_count = count_even_values(X)

# Displaying the result
print(f"The number of even values in the vector is: {even_count}")
