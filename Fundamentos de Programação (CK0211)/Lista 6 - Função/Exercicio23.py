'''Create a program that receives three values ​​(necessarily greater than zero), representing the measurements of the three sides of a triangle.
Create subroutines to:
■ determine whether these sides form a triangle (it is known that, to be a triangle, the measurement of a
any side must be less than or equal to the sum of the measurements of the other two).
■ determine and show the type of triangle (equilateral, isosceles or scalene), if the measurements form a triangle.
All messages must be shown in the main program'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# Receive input from the user
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check if it forms a triangle
if is_triangle(side1, side2, side3):
    # Determine the type of triangle
    triangle = triangle_type(side1, side2, side3)
    print(f"\nThe given sides form a {triangle} triangle.")
else:
    print("\nThe given sides do not form a triangle.")
