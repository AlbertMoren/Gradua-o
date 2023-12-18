'''Make a subroutine that receives two vectors of ten integers as parameters, determines and displays the intersection vector between them.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def intersection_vector(vector1, vector2):
    set1 = set(vector1)
    set2 = set(vector2)
    result = list(set1.intersection(set2))
    return result

# Input vectors from the user
vector1 = [int(input(f"Enter element {i+1} for vector1: ")) for i in range(10)]
vector2 = [int(input(f"Enter element {i+1} for vector2: ")) for i in range(10)]

# Calling the subroutine
result_vector = intersection_vector(vector1, vector2)

# Displaying the result
print("Intersection vector:", result_vector)
