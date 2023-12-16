'''Make a subroutine that takes a vector X of 20 of real numbers as a parameter and returns the sum
of the elements of'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def calculate_sum(vector):
    return sum(vector)

# Function to get user input for the vector
def input_vector(size):
    vector = []
    for i in range(size):
        element = float(input(f"Enter element {i + 1}: "))
        vector.append(element)
    return vector

# User inputs the data
n = 20
X = input_vector(n)

# Calling the subroutine
sum_result = calculate_sum(X)

# Displaying the result
print(f"The sum of the elements in the vector is: {sum_result}")
