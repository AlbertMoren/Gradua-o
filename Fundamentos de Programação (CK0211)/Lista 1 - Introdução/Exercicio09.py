# A program that calculates and displays the area of a trapezoid. It is known that: A = ((larger base + smaller base) * height) / 2

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

# Input the values for the larger base, smaller base, and height
larger_base, smaller_base, height = input("Enter the values for the larger base, smaller base, and height: ").split(" ")
larger_base = float(larger_base)
smaller_base = float(smaller_base)
height = float(height)

# Calculate and print the area of the trapezoid
area = ((larger_base + smaller_base) * height) / 2
print(f"The area of the trapezoid is {area}")
