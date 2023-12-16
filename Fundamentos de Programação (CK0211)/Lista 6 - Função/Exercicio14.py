'''Make a subroutine that takes a vector X of 30 integer elements as a parameter and returns two
vectors A and B. Vector A must contain the elements of X that are greater than zero and vector B, the elements smaller than or equal to zero.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def input_vector(size):
    vector = []
    for i in range(size):
        element = int(input(f"Enter element {i + 1}: "))
        vector.append(element)
    return vector

def separate_elements(x):
    a = [element for element in x if element > 0]
    b = [element for element in x if element <= 0]
    return a, b

# User inputs the data
n = 30
x = input_vector(n)

# Calling the subroutine
result_a, result_b = separate_elements(x)

# Displaying the results
print("Vector A (elements greater than zero):", result_a)
print("Vector B (elements less than or equal to zero):", result_b)

