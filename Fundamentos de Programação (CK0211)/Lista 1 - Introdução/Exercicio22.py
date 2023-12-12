'''Create a program that receives the number of sides of a convex polygon, calculates, and shows the number of diagonals of that polygon. It is known that ND = N * (N − 3)/2, where N is the number of sides of the polygon.'''

# My signature
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

def calculate_polygon_diagonals(n_sides):
    if n_sides < 3:
        return 0
    diagonals = n_sides * (n_sides - 3) / 2
    return diagonals

# Receive the number of sides of the polygon
n_sides = int(input("Enter the number of sides of the convex polygon: "))

# Calculate the number of diagonals
num_diagonals = calculate_polygon_diagonals(n_sides)

# Display the result
print(f"The number of diagonals of the convex polygon is: {num_diagonals}")
